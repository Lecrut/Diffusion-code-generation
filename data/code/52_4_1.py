import sys
def calculate_area(shape, length, width, radius, base, height):
    if shape == "rectangle":
        return length * width
    elif shape == "circle":
        return 3.14159 * radius * radius
    elif shape == "triangle":
        return 0.5 * base * height
    else:
        return "Invalid shape selected"
if __name__ == '__main__':
    shape = "rectangle"
    length = 10
    width = 5
    radius = 7
    base = 4
    height = 6
    area = calculate_area(shape, length, width, radius, base, height)
    print(f"Shape: {shape}")
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Radius: {radius}")
    print(f"Base: {base}")
    print(f"Height: {height}")
    print(f"Area: {area}")