def string_to_bool(string_list):
    return [s.lower() == 'true' for s in string_list]

if __name__ == '__main__':
    sample_values = ["True", "false", "TRUE", "  true  ", "", "False"]
    result = string_to_bool(sample_values)
    print(result)