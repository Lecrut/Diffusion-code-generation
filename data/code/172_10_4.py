def generate_reverse_mapping(word_to_key_map):
    reverse_map = {}
    for word, key in word_to_key_map.items():
        if key not in reverse_map:
            reverse_map[key] = word
    return reverse_map
if __name__ == '__main__':
    word_to_key_data = {
        "apple": "fruit_a",
        "banana": "fruit_b",
        "cherry": "fruit_a",
        "date": "fruit_c",
        "elderberry": "fruit_b"
    }
    reverse_mapping = generate_reverse_mapping(word_to_key_data)
    print(reverse_mapping)