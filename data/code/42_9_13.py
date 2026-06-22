class EllipseGeometry:
    PI_CONSTANT = 3.141592653589793

    @staticmethod
    def compute_area(semi_major_axis, semi_minor_axis):
        return EllipseGeometry.PI_CONSTANT * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    axis_a = 4.0
    axis_b = 2.5
    calculated_area = EllipseGeometry.compute_area(axis_a, axis_b)
    print(calculated_area)