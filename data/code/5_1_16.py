def compare_lengths(x, y):
    if x > y:
        return (1, x, y)
    elif x < y:
        return (-1, x, y)
    else:
        return (0, x, y)

if __name__ == '__main__':
    result = compare_lengths(3.5, 2.1)
    print(result)