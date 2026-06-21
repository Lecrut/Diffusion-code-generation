def sort_numerical_strings(numerical_strings):
    converted_integers = list(map(int, numerical_strings))
    sorted_integers = sorted(converted_integers)
    return sorted_integers

if __name__ == '__main__':
    sample_values = ["7", "3", "9", "2", "1"]
    sorted_values = sort_numerical_strings(sample_values)
    print(sorted_values)