class Card:
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.match = False

    def __eq__(self, other):
        return self.card == other.card

    def __str__(self):
        return self.card
