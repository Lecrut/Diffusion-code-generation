def min_numeric_string_value(str_list):
    return min(map(float, str_list))

if __name__ == '__main__':
    sample_values = ['3.5', '2.1', '4.8', '1.9']
    print(min_numeric_string_value(sample_values))