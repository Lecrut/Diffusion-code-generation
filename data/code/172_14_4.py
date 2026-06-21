nouns = {1: 'apple', 2: 'banana', 3: 'cherry'}

def get_noun(key):
    return nouns.get(key, None)
if __name__ == '__main__':
    print(get_noun(2))