def transform_shape(vertices, repetitions, translation_vectors):
    transformed_vertices = []
    for i in range(repetitions):
        translated_vertices = [(x + tx, y + ty) for x, y in vertices]
        transformed_vertices.extend(translated_vertices)
    return transformed_vertices

if __name__ == '__main__':
    sample_vertices = [(0, 0), (1, 0), (1, 1)]
    sample_repetitions = 3
    sample_translation_vectors = [(2, 2), (4, 4), (6, 6)]
    result = transform_shape(sample_vertices, sample_repetitions, sample_translation_vectors)
    print(result)