class NounMapper:
    def __init__(self):
        self.noun_mapping = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five'
        }

    def get_noun(self, key):
        return self.noun_mapping.get(key, "Key not found")

if __name__ == '__main__':
    mapper = NounMapper()
    print("Noun for Key 1:", mapper.get_noun(1))
    print("Noun for Key 6:", mapper.get_noun(6))