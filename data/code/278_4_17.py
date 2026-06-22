def print_dict_entries(dictionary):
    for key, value in dictionary.items():
        print(f'Key: {key}, Value: {value}')

if __name__ == '__main__':
    sample_data = {
        'name': 'Bob',
        'age': 30,
        'hobbies': ['reading', 'traveling', 'coding']
    }
    print_dict_entries(sample_data)