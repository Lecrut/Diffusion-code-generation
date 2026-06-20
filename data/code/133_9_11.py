def convert_to_bools(string_list):
    return [s.lower() == 'true' for s in string_list]

if __name__ == '__main__':
    sample_values = ['True', 'false', 'TRUE', 'False']
    print(convert_to_bools(sample_values))