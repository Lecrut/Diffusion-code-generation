def find_largest_element(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {
        "a": 10,
        "b": 42,
        "c": 7,
        "d": 99,
        "e": 23
    }
    result = find_largest_element(sample_data)
    print(result)