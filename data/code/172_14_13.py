nouns = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date', 5: 'elderberry'}

def get_noun(key):
    return nouns.get(key, 'unknown')
if __name__ == '__main__':
    print(get_noun(3))
    print(get_noun(6))