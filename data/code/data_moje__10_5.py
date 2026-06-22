def print_first_value(data):
    iterator = iter(data.values())
    try:
        print(next(iterator))
    except StopIteration:
        print()

if __name__ == '__main__':
    sample_dict = {'first': 10, 'second': 20, 'third': 30}
    print_first_value(sample_dict)