def get_first_item(iterable):
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError('The iterable is empty')

if __name__ == '__main__':
    sample_values = {
        'list': [10, 20, 30],
        'tuple': (40, 50, 60),
        'string': 'world'
    }
    
    for key, value in sample_values.items():
        print(f"First item of {key}: {get_first_item(value)}")