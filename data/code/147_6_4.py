def sort_numeric_strings(numeric_strings):
    return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sample_values = ["34", "12", "98", "56"]
    print(sort_numeric_strings(sample_values))