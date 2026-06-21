class NounMapper:
    NOUNS = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

    @staticmethod
    def get_noun(key):
        return NounMapper.NOUNS.get(key, None)

if __name__ == '__main__':
    mapper = NounMapper()
    for key in [1, 2, 3, 4, 5]:
        print(f"Key {key}: {mapper.get_noun(key)}")