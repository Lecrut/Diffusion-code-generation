def find_largest_value(items):
    if not items:
        raise ValueError("The list is empty")
    return max(items)

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2]
    try:
        largest = find_largest_value(data)
        print(largest)
    except ValueError as e:
        print(e)