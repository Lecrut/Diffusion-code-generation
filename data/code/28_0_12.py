def sort_pair(a, b):
    if a < b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    print(sort_pair(5, 2))
    print(sort_pair(3, 8))
    print(sort_pair(10, 10))