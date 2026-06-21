def get_initial_value(strings):
    return strings[0] if strings else None

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry']
    print(get_initial_value(sample_strings))