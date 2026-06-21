def sort_descending(a, b):
    if a > b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    print(sort_descending(3, 7))
    print(sort_descending(10, 2))
    print(sort_descending(5.5, 5.5))