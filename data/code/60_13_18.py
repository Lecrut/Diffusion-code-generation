def get_last_item(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    sample_values = {
        'fruits': ['apple', 'banana', 'cherry'],
        'numbers': [1, 2, 3, 4, 5],
        'colors': ['red', 'green', 'blue']
    }
    
    for category, items in sample_values.items():
        print(f"Last item in {category}: {get_last_item(items)}")