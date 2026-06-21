def sort_numerical_strings(numerical_strings):
    return sorted(map(int, numerical_strings))

if __name__ == '__main__':
    sample_values = ["10", "2", "30", "4", "50"]
    sorted_values = sort_numerical_strings(sample_values)
    print(sorted_values)