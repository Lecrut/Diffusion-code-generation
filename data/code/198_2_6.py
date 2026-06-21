def min_numeric_string_value(strings):
    return min(float(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["3.14", "2.718", "1.618"]
    print(min_numeric_string_value(sample_values))