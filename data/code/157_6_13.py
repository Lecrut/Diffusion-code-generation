def find_min_item(items):
    if not items:
        raise ValueError("The input list cannot be empty")
    return min((item for item in items))

if __name__ == '__main__':
    sample_items = [5, 3, 9, 1, 10]
    print(find_min_item(sample_items))