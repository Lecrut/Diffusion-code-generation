def sort_two(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_two(5, 3))
    print(sort_two(1, 2))
    print(sort_two(10, 10))