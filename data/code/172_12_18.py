def match_key_to_word(key_value_pairs):
    word_to_key = {}
    for key, value in key_value_pairs:
        word_to_key[key] = value
    return word_to_key

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "fruit1"),
        ("banana", "fruit2"),
        ("carrot", "vegetable1"),
        ("broccoli", "vegetable2")
    ]
    mapping = match_key_to_word(sample_pairs)
    print(f"Matching 'apple': {mapping.get('apple')}")
    print(f"Matching 'banana': {mapping.get('banana')}")
    print(f"Matching 'carrot': {mapping.get('carrot')}")
    print(f"Matching 'grape': {mapping.get('grape')}")