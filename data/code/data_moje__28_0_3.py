def sort_numbers(a, b):
    if a <= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    x = 5
    y = 2
    result = sort_numbers(x, y)
    print(result)