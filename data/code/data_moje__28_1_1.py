def sort_descending(a, b):
    values = [a, b]
    values.sort(reverse=True)
    return values

if __name__ == '__main__':
    x = 5
    y = 10
    result = sort_descending(x, y)
    print(result)