MAX_VALUE_ERROR = "Input list cannot be empty"

def find_greatest(items):
    if not items:
        raise ValueError(MAX_VALUE_ERROR)
    
    greatest_item = items[0]
    for item in items:
        if item > greatest_item:
            greatest_item = item
    
    return greatest_item

if __name__ == '__main__':
    sample_items = [3.14, 1.618, 2.718, 0.577, 9.99]
    try:
        result = find_greatest(sample_items)
        print(result)
    except ValueError as e:
        print(e)