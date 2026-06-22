def find_largest_item(items):
    largest = items[0]
    for item in items:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_items = [3.14, 2.71, 1.618, 0.577, 1.414]
    print(find_largest_item(sample_items))