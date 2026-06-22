def count_items(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    
    count = 0
    for item in items:
        count += 1
    
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"The number of items in the list is: {count_items(sample_list)}")