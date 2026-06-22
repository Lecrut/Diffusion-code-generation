def transform_shape(vertices, repetitions, translation_vectors):
    transformed_coords = []
    for i in range(repetitions):
        translated_vertex = [vertices[j] + translation_vectors[i][j] for j in range(len(vertices))]
        transformed_coords.append(translated_vertex)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetitions = 3
    translation_vectors = [(-1, -1), (0, 0), (1, 1)]
    print(transform_shape(vertices, repetitions, translation_vectors))