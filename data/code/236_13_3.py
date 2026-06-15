class ShapeRepeater:
    def generate_and_print(self, shape_type, repetitions):
        if shape_type == "right_angled_triangle":
            for i in range(repetitions):
                print(f"--- Triangle {i + 1} ---")
                print("Side A: 3")
                print("Side B: 4")
                print("Hypotenuse: 5")
        else:
            print(f"Unsupported shape type: {shape_type}")
if __name__ == '__main__':
    repeater = ShapeRepeater()
    shape_to_repeat = "right_angled_triangle"
    num_repetitions = 3
    repeater.generate_and_print(shape_to_repeat, num_repetitions)