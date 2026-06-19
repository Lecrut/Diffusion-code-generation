def compare_lengths(a, b):
    if a > b:
        return ('first', a)
    elif a < b:
        return ('second', b)
    else:
        return ('equal', a)

if __name__ == '__main__':
    result = compare_lengths(3.14, 2.71)
    print(result)