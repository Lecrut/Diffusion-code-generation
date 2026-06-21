class NounMapper:
    def __init__(self):
        self.noun_map = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five'
        }

    def get_noun(self, key):
        return self.noun_map.get(key)

if __name__ == '__main__':
    mapper = NounMapper()
    print("Noun for Key 1:", mapper.get_noun(1))
    print("Noun for Key 3:", mapper.get_noun(3))
    print("Noun for Key 5:", mapper.get_noun(5))