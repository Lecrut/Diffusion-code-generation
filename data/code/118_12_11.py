def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    vector_a = [2, 3, -4]
    vector_b = [5, -6, 7]
    result = dot_product(vector_a, vector_b)
    print(result)