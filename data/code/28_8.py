def sort_pair(a, b):
    if a > b:
        return (b, a)
    return (a, b)

if __name__ == '__main__':
    print(sort_pair(10, 5))
    print(sort_pair(3, 3))
    print(sort_pair(-1, 0))