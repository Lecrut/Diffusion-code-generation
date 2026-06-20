def compare_lengths(a, b):
    if a > b:
        return ('greater', a, b)
    elif a < b:
        return ('less', a, b)
    else:
        return ('equal', a, b)

if __name__ == '__main__':
    x = 5.5
    y = 3.2
    result = compare_lengths(x, y)
    print(result)