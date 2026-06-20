def convert_to_bool(strings):
    return [s.lower() == "true" for s in strings]

if __name__ == '__main__':
    sample_values = ["True", "false", "TRUE", "  true  ", "", "No"]
    print(convert_to_bool(sample_values))