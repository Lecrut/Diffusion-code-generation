def find_min_item(items):
    return min((item for item in items))

if __name__ == '__main__':
    sample_items = [7, 2, 5, 1, 3]
    print(find_min_item(sample_items))