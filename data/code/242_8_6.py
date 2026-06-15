import sys
def calculate_area(shape_type, length, width):
    if shape_type == "rectangle":
        return length * width
    elif shape_type == "circle":
        import math
        radius = length
        return math.pi * (radius ** 2)
    else:
        return 0
def main():
    data1 = {
        "shape": "rectangle",
        "length": 10,
        "width": 5
    }
    data2 = {
        "shape": "circle",
        "radius": 4
    }
    area1 = calculate_area(data1["shape"], data1["length"], data1["width"])
    area2 = calculate_area(data2["shape"], data2["radius"], 0)
    print(f"Shape 1 ({data1['shape']}) Area: {area1}")
    print(f"Shape 2 ({data2['shape']}) Area: {area2}")
    if area1 > area2:
        print("\nComparison Result:")
        print("Shape 1 has the greater area.")
    elif area2 > area1:
        print("\nComparison Result:")
        print("Shape 2 has the greater area.")
    else:
        print("\nComparison Result:")
        print("Both shapes have equal areas.")
if __name__ == '__main__':
    main()