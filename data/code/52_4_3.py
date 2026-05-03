import sys
def calculate_area(shape, length, width, radius, base, height):
    if shape == "rectangle":
        return length * width
    elif shape == "circle":
        return 3.14159 * radius * radius
    elif shape == "triangle":
        return 0.5 * base * height
    else:
        return 0
if __name__ == '__main__':
    shape_choice = "rectangle"
    length = 10
    width = 5
    radius = 7
    base = 4
    height = 6
    area = calculate_area(shape_choice, length, width, radius, base, height)
    print(f"Shape selected: {shape_choice}")
    print(f"Calculated Area: {area}")