def find_largest_item(data):
    if not data:
        raise ValueError("The input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    numbers = [10, 5, 20, 8, 35, 12]
    try:
        largest = find_largest_item(numbers)
        print(largest)
    except ValueError as e:
        print(e)