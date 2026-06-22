def compute_parallelogram_area(base_length: float, perpendicular_height: float) -> float:
    area_result = base_length * perpendicular_height
    return area_result

if __name__ == '__main__':
    sample_base = 12.5
    sample_height = 8.0
    computed_area = compute_parallelogram_area(sample_base, sample_height)
    print(computed_area)