def sort_numerical_strings(string_list):
    return sorted(map(int, string_list))

if __name__ == '__main__':
    sample_values = ['34', '12', '98', '56']
    print(sort_numerical_strings(sample_values))