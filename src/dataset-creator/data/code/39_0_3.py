def find_largest(lst):
    if not lst:
        raise ValueError("List is empty")
    return max(lst)
if __name__ == '__main__':
    sample_list = [34, 12, -5689.0357, 57]
    try:
        result = find_largest(sample_list)
        print(f"Largest item: {result}")
    except ValueError as e:
        print(e)