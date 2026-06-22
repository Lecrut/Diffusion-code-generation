def find_largest_item(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the list must be numbers")
    return max(data)

if __name__ == '__main__':
    numbers = [10, 5, 20, 8, 35, 12]
    largest = find_largest_item(numbers)
    print(largest)