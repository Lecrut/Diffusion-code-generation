def find_maximum(dictionary):
    if not dictionary:
        raise ValueError("Dictionary is empty")
    return max(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5}
    result = find_maximum(sample_dict)
    print(result)