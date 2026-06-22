def transform_shape(vertices, repetitions, translation_vectors):
    transformed_shapes = []
    for i in range(repetitions):
        translated_vertices = [(v[0] + tv[0], v[1] + tv[1]) for v, tv in zip(vertices, translation_vectors)]
        transformed_shapes.append(translated_vertices)
    return transformed_shapes

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetitions = 3
    translation_vectors = [(2, 2), (4, 4), (6, 6)]
    print(transform_shape(vertices, repetitions, translation_vectors))