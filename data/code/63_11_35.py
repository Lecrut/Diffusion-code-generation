def get_first_item(iterable):
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError('The iterable is empty')

if __name__ == '__main__':
    sample_data = {
        'numbers': [1, 2, 3],
        'letters': ('a', 'b', 'c'),
        'characters': 'python'
    }
    
    for category, items in sample_data.items():
        print(f"First item of {category}: {get_first_item(items)}")