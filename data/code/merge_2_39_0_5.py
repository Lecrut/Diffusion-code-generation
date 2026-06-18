def find_largest_item(items):
    if not items:
        raise ValueError("Error: List is empty.")
    return max(items)
if __name__ == '__main__':
    sample_list = [10, 5, 23, 89, 4]
    try:
        result = find_largest_item(sample_list)
        print(f"The largest item is {result}")
    except ValueError as e:
        print(e)