def validate_input(vertices, repetition_count, translation_vectors):
    if len(vertices) == 0 or len(vertices[0]) != 2:
        raise ValueError("Vertices must be a list of tuples representing 2D points.")
    if repetition_count <= 0:
        raise ValueError("Repetition count must be greater than zero.")
    if len(translation_vectors) != repetition_count:
        raise ValueError("Translation vectors list length must match repetition count.")

def transform_shape(vertices, repetition_count, translation_vectors):
    validate_input(vertices, repetition_count, translation_vectors)
    transformed_coords = []
    for i in range(repetition_count):
        translated_vertex = [vertices[j] + translation_vectors[i][j] for j in range(len(vertices))]
        transformed_coords.append(translated_vertex)
    return transformed_coords

if __name__ == '__main__':
    vertices = [(0, 0), (1, 0), (1, 1)]
    repetition_count = 3
    translation_vectors = [(2, 2), (3, 3), (4, 4)]
    print(transform_shape(vertices, repetition_count, translation_vectors))