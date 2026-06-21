def sort_numerical_strings(lst):
    return sorted(map(int, lst))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "2"]
    print(sort_numerical_strings(sample_values))