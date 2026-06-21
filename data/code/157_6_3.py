def find_min_item(items):
    return min((item for item in items))

if __name__ == '__main__':
    sample_items = [8, 2, 7, 3, 6]
    print(find_min_item(sample_items))