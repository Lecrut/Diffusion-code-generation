def sort_numeric_strings(lst):
    return sorted(lst, key=int)

if __name__ == '__main__':
    sample_values = ["3", "12", "5", "100"]
    print(sort_numeric_strings(sample_values))