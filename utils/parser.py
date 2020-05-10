from bencoding.decoder import Decoder
from bencoding.encoder import Encoder


class Parser:
    def __init__(self):
        self.decoder = Decoder()
        self.encoder = Encoder()
