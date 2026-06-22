def transform_shape(vertices, translation_vectors):
    return [[v + t for v, t in zip(vertex, vector)] for vertex, vector in zip(vertices, translation_vectors * len(vertices))]

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    translation_vectors = [(2, 3), (4, 5)]
    transformed_vertices = transform_shape(vertices, translation_vectors)
    print(transformed_vertices)