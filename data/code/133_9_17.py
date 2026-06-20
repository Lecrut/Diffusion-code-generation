def convert_to_bools(str_list):
    return [bool(val.lower()) for val in str_list]

if __name__ == '__main__':
    sample_values = ['True', 'false', 'TRUE', 'FALSE']
    print(convert_to_bools(sample_values))