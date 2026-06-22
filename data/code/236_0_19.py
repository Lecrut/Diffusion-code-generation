def transform_shape(vertices, repetitions, translation_vectors):
    transformed_coords = []
    for i in range(repetitions):
        translated_coords = [(x + tx, y + ty) for x, y in vertices]
        transformed_coords.extend(translated_coords)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetitions = 3
    translation_vectors = [(2, 2), (4, 4), (6, 6)]
    result = transform_shape(vertices, repetitions, translation_vectors)
    print(result)