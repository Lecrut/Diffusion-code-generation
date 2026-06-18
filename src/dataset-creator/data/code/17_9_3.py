import math
def calculate_area(length: float, width: float) -> float:
    return length * width
def calculate_circumference(radius: float) -> float:
    return 2 * math.pi * radius
def main():
    sample_length = 10.0
    sample_width = 5.0
    sample_radius = 7.0
    area = calculate_area(sample_length, sample_width)
    circumference = calculate_circumference(sample_radius)
    print(f"Sample Length: {sample_length}")
    print(f"Sample Width: {sample_width}")
    print(f"Calculated Area: {area}")
    print("-" * 20)
    print(f"Sample Radius: {sample_radius}")
    print(f"Calculated Circumference: {circumference}")
if __name__ == '__main__':
    main()