def iterate_and_print(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':
    sample_dict = {'foo': 'bar', 'baz': 42, 'qux': True}
    iterate_and_print(sample_dict)