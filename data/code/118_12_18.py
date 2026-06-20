def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    vector_a = [1, 3, -5]
    vector_b = [4, -2, -1]
    result = dot_product(vector_a, vector_b)
    print(result)