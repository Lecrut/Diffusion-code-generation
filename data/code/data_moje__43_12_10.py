def calculate_pyramid_surface_area(base_length: float, lateral_edge_length: float) -> float:
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError("Base length and lateral edge length must be positive")
    if lateral_edge_length <= (base_length / 2):
        raise ValueError("Lateral edge length must be sufficient to form a pyramid")
    base_area = base_length * base_length
    half_base = base_length / 2
    slant_height = (lateral_edge_length**2 - half_base**2)**0.5
    triangular_face_area = 0.5 * base_length * slant_height
    lateral_area = 4 * triangular_face_area
    return base_area + lateral_area

if __name__ == '__main__':
    sample_base = 10.0
    sample_lateral_edge = 13.0
    result = calculate_pyramid_surface_area(sample_base, sample_lateral_edge)
    print(result)