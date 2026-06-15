def find_smallest():
    data = [10, 5, 20, 3, 15]
    if not data:
        return None
    smallest = data[0]
    for number in data:
        if number < smallest:
            smallest = number
    return smallest
if __name__ == '__main__':
    result = find_smallest()
    print(result)