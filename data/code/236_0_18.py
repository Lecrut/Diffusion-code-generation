def transform_shape(vertices, repetition_count, translation_vectors):
    transformed_vertices = []
    for i in range(repetition_count):
        translated_vertex = [v + t for v, t in zip(vertices, translation_vectors[i])]
        transformed_vertices.append(translated_vertex)
    return transformed_vertices

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetition_count = 3
    translation_vectors = [[2, 2], [4, 4], [6, 6]]
    print(transform_shape(vertices, repetition_count, translation_vectors))