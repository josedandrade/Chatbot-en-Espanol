import os
corpus = "./data/es.txt"
corpus_name = "OpenSubtitle"
save_dir = os.path.join("data", "models")

MAX_LENGTH = 20        # Tamaño de las frases
LINES_USED = 2_500_000 # Determina el tamaño de la parte de dataset que cogemos
MIN_COUNT  = 5         # Minimum word count threshold for trimming
WITH_UNK   = True      # Swap words not in voc for unk token, instead of deleting sentence
if WITH_UNK: corpus_name += "_UNK"

PAD_token = 0  # Used for padding short sentences
SOS_token = 1  # Start-of-sentence token
EOS_token = 2  # End-of-sentence token
UNK_token = 3