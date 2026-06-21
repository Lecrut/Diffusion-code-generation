def find_min_item(items):
    return min((item for item in items))

if __name__ == '__main__':
    sample_items = [7, 2, 5, 4, 3]
    min_value = find_min_item(sample_items)
    print(min_value)