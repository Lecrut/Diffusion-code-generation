def sort_pair(a, b):
    return (min(a, b), max(a, b))

if __name__ == '__main__':
    print(sort_pair(10, 5))
    print(sort_pair(3, 7))
    print(sort_pair(0, 0))