def transform_shape(vertices, repetitions, translation_vectors):
    transformed_coords = []
    for i in range(repetitions):
        translated_vertex = [v + t for v, t in zip(vertices, translation_vectors[i])]
        transformed_coords.append(translated_vertex)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetitions = 3
    translation_vectors = [[2, 2], [4, 4], [6, 6]]
    print(transform_shape(vertices, repetitions, translation_vectors))