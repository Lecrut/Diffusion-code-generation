def find_smallest_int_string(strings):
    return min(strings, key=int)

if __name__ == '__main__':
    sample_strings = ["3", "2", "5", "1"]
    print(find_smallest_int_string(sample_strings))