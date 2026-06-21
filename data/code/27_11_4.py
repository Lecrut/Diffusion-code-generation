class TriangleValidator:
    def __init__(self, side_sets):
        self.side_sets = side_sets

    def validate_all(self):
        results = []
        for sides in self.side_sets:
            if not isinstance(sides, (list, tuple)) or len(sides) != 3:
                results.append(False)
                continue
            a, b, c = sides
            if a <= 0 or b <= 0 or c <= 0:
                results.append(False)
                continue
            sorted_sides = sorted([a, b, c])
            valid = sorted_sides[0] + sorted_sides[1] > sorted_sides[2]
            results.append(valid)
        return results

if __name__ == '__main__':
    sample_data = [
        [3, 4, 5],
        [1, 2, 3],
        [10, 15, 20],
        [1, 1, 1],
        [0, 4, 5],
        [-1, 2, 3],
        [1, 100, 100],
        [7, 8, 9]
    ]
    validator = TriangleValidator(sample_data)
    print(validator.validate_all())