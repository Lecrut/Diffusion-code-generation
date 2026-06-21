def check_duplicates(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    return len(input_string) != len(set(input_string))

if __name__ == '__main__':
    _sample_var = "Python"
    _result_val = check_duplicates(_sample_var)
    print(_result_val)