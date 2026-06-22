def transform_shape(vertices, repetitions, translation_vectors):
    transformed_coords = []
    for i in range(repetitions):
        translated_vertices = [(x + tx, y + ty) for x, y, tx, ty in zip(vertices, [0]*len(vertices), translation_vectors)]
        transformed_coords.append(translated_vertices)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(1, 2), (3, 4), (5, 6)]
    repetitions = 3
    translation_vectors = [(10, 20), (30, 40), (50, 60)]
    result = transform_shape(vertices, repetitions, translation_vectors)
    print(result)