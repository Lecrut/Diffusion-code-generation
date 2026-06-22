def max_tuples(tup1, tup2):
    return tuple(max(a, b) for a, b in zip(tup1, tup2))

if __name__ == '__main__':
    result = max_tuples((1, 3, 5), (2, 2, 6))
    print(result)