def sort_numeric_strings(numeric_strings):
    numeric_map = {str(i): i for i in range(10)}
    return sorted(map(int, numeric_strings), key=lambda x: [numeric_map[digit] for digit in str(x)])

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numeric_strings(sample_values))