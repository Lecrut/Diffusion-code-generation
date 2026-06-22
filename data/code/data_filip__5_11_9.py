def process_strings(input_tuple):
    return tuple(s.capitalize() for s in input_tuple)

if __name__ == '__main__':
    sample_data = ('hElLo', 'woRLD', 'PyThOn', 'tEST')
    result = process_strings(sample_data)
    print(result)