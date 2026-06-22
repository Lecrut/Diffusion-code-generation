sample_list = ['apple', 'banana', 'cherry']

def print_items(items):
    if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
        raise ValueError("Input must be a list of strings")
    
    [print(item) for item in items]

if __name__ == '__main__':
    print_items(sample_list)