class ShapeRepeater:
    def generate_and_print_triangle(self, shape_type, repetitions):
        if shape_type == "right-angled triangle":
            for i in range(repetitions):
                print(f"--- Triangle {i + 1} ---")
                print("Side A: 3")
                print("Side B: 4")
                print("Hypotenuse: 5")
                print("-" * 20)
        else:
            print(f"Unsupported shape type: {shape_type}")
if __name__ == '__main__':
    repeater = ShapeRepeater()
    shape = "right-angled triangle"
    n = 3
    repeater.generate_and_print_triangle(shape, n)