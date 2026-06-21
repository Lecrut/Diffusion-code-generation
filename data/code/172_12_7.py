class KeyWordMapper:
    def __init__(self, words, keys):
        if len(words) != len(keys):
            raise ValueError("Word and key lists must have the same length")
        self._mapping = {word: key for word, key in zip(words, keys)}

    def get_key_for_word(self, word):
        return self._mapping.get(word)

if __name__ == '__main__':
    words = ["apple", "banana", "cherry", "date"]
    keys = ["A1", "B2", "C3", "D4"]
    
    mapper = KeyWordMapper(words, keys)
    print(f"Key for 'apple': {mapper.get_key_for_word('apple')}")
    print(f"Key for 'banana': {mapper.get_key_for_word('banana')}")
    print(f"Key for 'grape': {mapper.get_key_for_word('grape')}")
    print(f"Key for 'date': {mapper.get_key_for_word('date')}")