class AttributeValidator:
    def validate(self, x, y, z):
        is_x_positive = x > 0
        is_y_even = y % 2 == 0
        is_z_divisible_by_xy = x != 0 and z % (x * y) == 0
        return is_x_positive and is_y_even and is_z_divisible_by_xy

if __name__ == '__main__':
    validator = AttributeValidator()
    print(f"Test 1 (x=2, y=4, z=8): {validator.validate(2, 4, 8)}")
    print(f"Test 2 (x=-1, y=2, z=4): {validator.validate(-1, 2, 4)}")
    print(f"Test 3 (x=3, y=5, z=9): {validator.validate(3, 5, 9)}")
    print(f"Test 4 (x=2, y=3, z=6): {validator.validate(2, 3, 6)}")