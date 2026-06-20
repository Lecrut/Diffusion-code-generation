def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    print(dot_product([1, 2, 3], [4, 5, 6]))