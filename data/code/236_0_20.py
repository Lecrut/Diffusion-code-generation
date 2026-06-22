def transform_shape(vertices, repetition_count, translation_vectors):
    transformed_coords = []
    for i in range(repetition_count):
        translated_coords = [(x + tx, y + ty) for x, y in vertices for tx, ty in translation_vectors]
        transformed_coords.extend(translated_coords)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetition_count = 2
    translation_vectors = [(0, 0), (2, 0), (0, 2)]
    result = transform_shape(vertices, repetition_count, translation_vectors)
    print(result)