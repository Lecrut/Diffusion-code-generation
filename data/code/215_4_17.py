def find_largest_value(dictionary):
    if not dictionary:
        raise ValueError("Dictionary cannot be empty")
    return max(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    print(f"Largest value in dictionary: {find_largest_value(sample_dict)}")