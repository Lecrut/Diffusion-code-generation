def get_last_item(data):
    return data[-1] if data else None

if __name__ == '__main__':
    sample_lists = {
        'numbers': [1, 2, 3, 4, 5],
        'letters': ['a', 'b', 'c'],
        'empty': [],
        'single': [99]
    }
    
    for name, lst in sample_lists.items():
        last_element = get_last_item(lst)
        print(f"Last item of {name} list: {last_element}")