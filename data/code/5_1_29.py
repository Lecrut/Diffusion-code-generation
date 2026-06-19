def compare_lengths(a, b):
    if a > b:
        return ('a', 'greater')
    elif a < b:
        return ('b', 'greater')
    else:
        return ('equal',)

if __name__ == '__main__':
    result = compare_lengths(3.14, 2.71)
    print(result)