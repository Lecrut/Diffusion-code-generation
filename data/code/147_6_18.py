def sort_numeric_strings(numeric_strings):
    return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sample_values = ["7", "3", "10", "2"]
    print(sort_numeric_strings(sample_values))