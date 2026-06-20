def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    vector1 = [1, 3, -5]
    vector2 = [4, -2, -1]
    result = dot_product(vector1, vector2)
    print(result)