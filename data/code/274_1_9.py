def print_list_items(iterable):
    for item in iterable:
        print(item)

if __name__ == '__main__':
    sample_values = {
        'numbers': [1, 2, 3],
        'strings': ["apple", "banana"],
        'mixed': [4.5, True, None]
    }
    
    for category, items in sample_values.items():
        print(f"\nCategory: {category}")
        print_list_items(items)