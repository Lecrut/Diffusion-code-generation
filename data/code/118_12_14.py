def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    vector_a = [7, 5, -3]
    vector_b = [2, -4, 6]
    result = dot_product(vector_a, vector_b)
    print(result)