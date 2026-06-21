def min_numeric_string_value(string_list):
    return min(float(value) for value in string_list)

if __name__ == '__main__':
    sample_values = ["3.5", "2.1", "4.8", "1.9"]
    print(min_numeric_string_value(sample_values))