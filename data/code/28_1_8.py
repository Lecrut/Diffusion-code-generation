def sort_descending(a, b):
    if a < b:
        return [b, a]
    return [a, b]

if __name__ == '__main__':
    x = 10
    y = 20
    result = sort_descending(x, y)
    print(result)