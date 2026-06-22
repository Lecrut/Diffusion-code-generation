def sort_descending(a, b):
    if a >= b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    x = 10
    y = 5
    result = sort_descending(x, y)
    print(result)