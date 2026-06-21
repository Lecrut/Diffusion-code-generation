NUMERIC_STRING_TO_FLOAT = float

def min_numeric_string_value(lst):
    return NUMERIC_STRING_TO_FLOAT(min(lst))

if __name__ == '__main__':
    sample_values = ['3.14', '2.718', '1.618', '0.577']
    print(min_numeric_string_value(sample_values))