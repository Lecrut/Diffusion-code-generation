def transform_shape(vertices, translation_vectors):
    return [[x + tx, y + ty] for (x, y), (tx, ty) in zip(vertices, translation_vectors * len(vertices))]

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    translation_vectors = [(2, 3), (4, 5)]
    print(transform_shape(vertices, translation_vectors))