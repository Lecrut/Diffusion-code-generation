def find_largest_value(items):
    if not items:
        raise ValueError("List is empty")
    
    largest = items[0]
    for item in items[1:]:
        if item > largest:
            largest = item
    
    return largest

if __name__ == '__main__':
    data = [7, 3, 9, 2, 5, 6]
    try:
        largest = find_largest_value(data)
        print(largest)
    except ValueError as e:
        print(e)