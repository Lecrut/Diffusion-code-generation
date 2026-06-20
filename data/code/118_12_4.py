def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(dot_product(v1, v2))