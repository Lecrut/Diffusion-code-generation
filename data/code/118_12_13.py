def validate_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    return v1, v2

def dot_product(v1, v2):
    validated_vectors = validate_vectors(v1, v2)
    return sum(x * y for x, y in zip(*validated_vectors))

if __name__ == '__main__':
    vector1 = [1, 3, -5]
    vector2 = [4, -2, -1]
    result = dot_product(vector1, vector2)
    print(result)