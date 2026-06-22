def find_largest_item(data):
    return max(data)

if __name__ == '__main__':
    numbers = [10, 5, 20, 8, 15]
    largest = find_largest_item(numbers)
    print(largest)