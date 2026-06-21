def find_smallest_int_string(strings):
    return min(strings, key=int)

if __name__ == '__main__':
    sample_strings = ["100", "25", "37", "4"]
    result = find_smallest_int_string(sample_strings)
    print(result)