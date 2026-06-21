def sort_numerical_strings(string_list):
    return sorted(map(int, string_list))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numerical_strings(sample_values))