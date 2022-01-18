import config
import transformers
import torch.nn as nn


class BERTBaseUncased(nn.Module):
    def __init__(self):
        super().__init__()
        self.bert = transformers.BertModel.from_pretrained(config.BERT_PATH)
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768, 1)

    def forward(self, ids, mask, token_type_ids):
        outputs = self.bert(
            ids,
            attention_mask=mask,
            token_type_ids=token_type_ids
        )
        bert_output = self.bert_drop(outputs["pooler_output"])
        output = self.out(bert_output)
        return output
