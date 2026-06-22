def print_list_items(iterable):
    for item in iterable:
        print(item)

if __name__ == '__main__':
    sample_data = {
        'list': [1, "hello", 3.14, True],
        'tuple': ('a', 'b', 'c'),
        'string': "Hello",
        'nested_list': [[5, 6]]
    }
    
    for key, value in sample_data.items():
        print(f"Printing {key}:")
        print_list_items(value)