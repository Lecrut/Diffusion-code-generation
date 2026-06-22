def sort_descending(a, b):
    if a >= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    x = 15
    y = 42
    result = sort_descending(x, y)
    print(result)