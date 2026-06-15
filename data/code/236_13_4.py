class ShapeRepeater:
    def generate_and_print_triangle(self, shape_type, repetitions):
        if shape_type == "right-angled triangle":
            for i in range(repetitions):
                print(f"--- Triangle {i + 1} ---")
                print("Side A: 3 units")
                print("Side B: 4 units")
                print("Hypotenuse: 5 units")
        else:
            print(f"Unsupported shape type: {shape_type}")
if __name__ == '__main__':
    repeater = ShapeRepeater()
    shape_to_repeat = "right-angled triangle"
    num_repetitions = 3
    repeater.generate_and_print_triangle(shape_to_repeat, num_repetitions)