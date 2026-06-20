def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == '__main__':
    vectorA = [7, 5, -3]
    vectorB = [2, -4, 6]
    result = dot_product(vectorA, vectorB)
    print(result)