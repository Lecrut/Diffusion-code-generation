def sort_numerical_strings(strings):
    return sorted(map(int, strings))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numerical_strings(sample_values))