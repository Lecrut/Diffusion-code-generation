def find_smallest(data):
    return min(data)

if __name__ == '__main__':
    numbers = [42, 15, 89, 3, 77, 101]
    smallest = find_smallest(numbers)
    print(smallest)