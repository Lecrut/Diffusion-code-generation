def find_smallest_int_string(strings):
    return min(strings, key=int)

if __name__ == '__main__':
    sample_strings = ["42", "7", "13", "9"]
    result = find_smallest_int_string(sample_strings)
    print(result)