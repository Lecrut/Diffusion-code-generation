def transform_shape(vertices, repetition_count, translation_vectors):
    transformed_coords = []
    for i in range(repetition_count):
        translated_vertex = [vertices[j] + translation_vectors[i][j] for j in range(len(vertices))]
        transformed_coords.append(translated_vertex)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (0, 1)]
    repetition_count = 3
    translation_vectors = [(1, 1), (2, 2), (3, 3)]
    print(transform_shape(vertices, repetition_count, translation_vectors))