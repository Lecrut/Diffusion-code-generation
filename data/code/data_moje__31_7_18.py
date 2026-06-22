def compute_square_areas(side_lengths):
    def validate_and_square(side):
        if not isinstance(side, (int, float)):
            raise TypeError("Side length must be a number")
        if side < 0:
            raise ValueError("Side length must be non-negative")
        return side ** 2
    return [validate_and_square(side) for side in side_lengths]

if __name__ == '__main__':
    sample_sides = [3, 5, 7, 9]
    computed_areas = compute_square_areas(sample_sides)
    print(computed_areas)