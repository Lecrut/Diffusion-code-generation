def convert_to_bool(lst):
    return [s.lower() == 'true' for s in lst]

if __name__ == '__main__':
    sample_values = ['True', 'false', 'TRUE', 'False']
    print(convert_to_bool(sample_values))