def print_first_value(data):
    first_value = next(iter(data.values()))
    print(first_value)

if __name__ == '__main__':
    sample_dict = {'alpha': 10, 'beta': 20, 'gamma': 30}
    print_first_value(sample_dict)