def sort_descending(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_descending(10, 20))
    print(sort_descending(30, 15))
    print(sort_descending(5, 5))