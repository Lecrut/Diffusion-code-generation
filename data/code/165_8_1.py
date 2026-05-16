import math
def calculate_area(length, width):
    return length * width
def calculate_circumference(radius):
    return 2 * math.pi * radius
def main():
    print("--- Area Calculation ---")
    sample_length = 10.5
    sample_width = 5.0
    area = calculate_area(sample_length, sample_width)
    print(f"Sample Length: {sample_length}")
    print(f"Sample Width: {sample_width}")
    print(f"Calculated Area: {area}")
    print("\n--- Circumference Calculation ---")
    sample_radius = 7.0
    circumference = calculate_circumference(sample_radius)
    print(f"Sample Radius: {sample_radius}")
    print(f"Calculated Circumference: {circumference}")
if __name__ == '__main__':
    main()