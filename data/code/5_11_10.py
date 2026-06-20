def process_strings(input_tuple):
    return tuple(s.capitalize() for s in input_tuple)

if __name__ == '__main__':
    sample_input = ("hElLo", "wOrLd", "PyThOn", "tEsT")
    result = process_strings(sample_input)
    print(result)