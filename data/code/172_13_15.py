def create_key_value_dict(words):
    return {word: chr(65 + idx) for idx, word in enumerate(words)}

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    key_value_dict = create_key_value_dict(sample_words)
    print(key_value_dict)