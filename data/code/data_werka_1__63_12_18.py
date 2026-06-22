def get_first_item(iterable):
    return next(iter(iterable), None)

if __name__ == '__main__':
    sample_data = {
        'list': [1, 2, 3],
        'tuple': (4, 5, 6),
        'string': 'hello',
        'empty_list': [],
    }
    
    for key, value in sample_data.items():
        print(f"First item of {key}: {get_first_item(value)}")