def sort_numeric_strings(lst):
    return sorted(lst, key=lambda x: int(x))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "2"]
    print(sort_numeric_strings(sample_values))