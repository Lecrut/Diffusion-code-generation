def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    vec1 = [1, 3, -5]
    vec2 = [4, -2, -1]
    print(dot_product(vec1, vec2))