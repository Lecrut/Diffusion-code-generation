def sort_descending(a, b):
    if a >= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    result = sort_descending(10, 5)
    print(result)
    result = sort_descending(3, 8)
    print(result)
    result = sort_descending(7.5, 2.1)
    print(result)
    result = sort_descending(-5, -10)
    print(result)
    result = sort_descending(42, 42)
    print(result)