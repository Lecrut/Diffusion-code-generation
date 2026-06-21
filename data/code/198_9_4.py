def find_smallest_int_string(strings):
    return min(strings, key=int)

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(find_smallest_int_string(sample_values))