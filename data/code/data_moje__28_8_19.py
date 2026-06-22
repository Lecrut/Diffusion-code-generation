def sort_pair(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_pair(5, 3))
    print(sort_pair(1, 10))
    print(sort_pair(-2, 4))
    print(sort_pair(7, 7))