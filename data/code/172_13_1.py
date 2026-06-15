def construct_dictionary(data):
    result = {}
    for word, key in data:
        result[word] = key
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "A"),
        ("banana", "B"),
        ("cherry", "C"),
        ("date", "D")
    ]
    output = construct_dictionary(sample_data)
    print(output)