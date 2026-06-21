def create_sample_list():
    sample_items = [
        {'name': 'apple', 'type': 'fruit', 'quantity': 42},
        {'name': 'banana', 'type': 'fruit', 'quantity': 99},
        {'name': 'cherry', 'type': 'fruit', 'quantity': 101},
        {'name': 'date', 'type': 'fruit', 'quantity': 55},
        {'name': 'elderberry', 'type': 'fruit', 'quantity': 200}
    ]
    return sample_items

if __name__ == '__main__':
    my_list = create_sample_list()
    for item in my_list:
        print(item)