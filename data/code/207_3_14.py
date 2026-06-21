def find_maximum(dictionary):
    if not dictionary:
        return None
    return max(dictionary.values())

if __name__ == '__main__':
    input_data = {'a': 15, 'b': 8, 'c': 22, 'd': 4, 'e': 30, 'f': 11}
    result = find_maximum(input_data)
    print(result)