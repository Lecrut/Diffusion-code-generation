def transform_shape(vertices, repetition_count, translation_vectors):
    transformed_vertices = []
    for i in range(repetition_count):
        translated_vertex = [vertices[j] + translation_vectors[i][j] for j in range(len(vertices))]
        transformed_vertices.append(translated_vertex)
    return transformed_vertices

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetition_count = 3
    translation_vectors = [(2, 2), (3, 3), (4, 4)]
    print(transform_shape(vertices, repetition_count, translation_vectors))