def sort_two_integers(a, b):
    if a <= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    x = 42
    y = 17
    result = sort_two_integers(x, y)
    print(result)