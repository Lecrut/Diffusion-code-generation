def find_middle(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]
if __name__ == '__main__':
    print(find_middle(1, 2, 3))
    print(find_middle(3, 1, 2))
    print(find_middle(5, 2, 8))
    print(find_middle(-10, 0, 5))
    print(find_middle(100, 100, 100))