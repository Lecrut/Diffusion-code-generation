def sort_pair(a, b):
    return (min(a, b), max(a, b))

if __name__ == '__main__':
    print(sort_pair(5, 3))
    print(sort_pair(10, 10))
    print(sort_pair(-1, -5))
    print(sort_pair(0, 42))