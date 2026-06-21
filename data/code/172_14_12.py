nouns = {1: 'apple', 2: 'banana', 3: 'cherry'}

def get_noun(key):
    return nouns.get(key, 'unknown')
if __name__ == '__main__':
    print(get_noun(1))
    print(get_noun(4))