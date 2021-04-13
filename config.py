import transformers
from transformers import BertTokenizer

DEVICE = "cpu"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = './input/bert_base_uncased'
MODEL_PATH = "model.bin"
TRAINING_FILE = ".\input\IMDB_Dataset.xlsx"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True)
