def display_dict_entries(data):
    for entry_key, entry_value in data.items():
        print(f"Key: {entry_key}, Value: {entry_value}")

if __name__ == '__main__':
    sample_dictionary = {'foo': 42, 'bar': 3.14, 'baz': True}
    display_dict_entries(sample_dictionary)