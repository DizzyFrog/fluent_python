import collections

Card = collections.namedtuple('card',['rank','suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list['JQKA']
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = []