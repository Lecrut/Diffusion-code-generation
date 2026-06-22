def print_values_by_key(dict_list, key):
    for dictionary in dict_list:
        if key in dictionary:
            print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'title': 'Python Programming', 'author': 'John Doe'},
        {'title': 'Data Science Essentials', 'author': 'Jane Smith'},
        {'title': 'Machine Learning Fundamentals', 'author': 'Alice Johnson'}
    ]
    key_to_print = 'title'
    print_values_by_key(sample_dicts, key_to_print)