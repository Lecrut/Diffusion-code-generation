def calculate_ratio():
    length1 = 15
    length2 = 25
    smallest = min(length1, length2)
    largest = max(length1, length2)
    ratio = largest / smallest
    return ratio
if __name__ == '__main__':
    result = calculate_ratio()
    print(result)