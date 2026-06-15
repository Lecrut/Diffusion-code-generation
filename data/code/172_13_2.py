def construct_dictionary(data):
    result = {}
    for word, key in data:
        result[word] = key
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "fruit"),
        ("banana", "fruit"),
        ("carrot", "vegetable"),
        ("broccoli", "vegetable"),
        ("grape", "fruit")
    ]
    output_dict = construct_dictionary(sample_data)
    print(output_dict)