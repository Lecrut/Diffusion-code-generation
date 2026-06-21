def sort_numerical_strings(numerical_strings):
    return sorted(map(int, numerical_strings))

if __name__ == '__main__':
    sample_values = ['34', '12', '90', '5']
    print(sort_numerical_strings(sample_values))