def generate_reverse_mapping(word_to_key_map):
    reverse_map = {}
    for word, key in word_to_key_map.items():
        reverse_map[key] = word
    return reverse_map
if __name__ == '__main__':
    sample_data = {
        "apple": "fruit_a",
        "banana": "fruit_b",
        "carrot": "vegetable_x",
        "spinach": "vegetable_y"
    }
    reverse_mapping = generate_reverse_mapping(sample_data)
    print(reverse_mapping)