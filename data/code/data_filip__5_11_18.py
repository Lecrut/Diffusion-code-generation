def capitalize_mixed_case_strings(data_tuple):
    return tuple(s.capitalize() for s in data_tuple)

if __name__ == '__main__':
    sample_input = ("hELLO", "wOrld", "PyThOn", "tEst")
    result = capitalize_mixed_case_strings(sample_input)
    print(result)