def capitalize_mixed_case_strings(input_tuple):
    return tuple(s.capitalize() for s in input_tuple)

if __name__ == '__main__':
    sample_data = ("hELLO", "worLD", "PyThOn", "tEsT")
    result = capitalize_mixed_case_strings(sample_data)
    print(result)