def bool_convert(lst):
    return [s.lower() == 'true' for s in lst]

if __name__ == '__main__':
    sample_values = ['True', 'false', 'TRUE', '  true  ', '', 'No']
    print(bool_convert(sample_values))