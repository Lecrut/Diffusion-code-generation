def retrieve_first_item(collection):
    return collection[0]

if __name__ == '__main__':
    test_data = {
        'fruits': ['apple', 'banana', 'cherry'],
        'numbers': [1, 2, 3, 4, 5],
        'colors': ['red', 'green', 'blue']
    }
    
    for category, items in test_data.items():
        first_item = retrieve_first_item(items)
        print(f"The first item in the {category} category is: {first_item}")