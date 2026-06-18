import math
def calculate_area(length: float, width: float) -> float:
    return length * width
def calculate_circumference(radius: float) -> float:
    return 2 * math.pi * radius
def main():
    length_sample = 10.0
    width_sample = 5.0
    radius_sample = 7.0
    area_result = calculate_area(length_sample, width_sample)
    circumference_result = calculate_circumference(radius_sample)
    print(f"Sample Length: {length_sample}")
    print(f"Sample Width: {width_sample}")
    print(f"Calculated Area: {area_result}")
    print("-" * 20)
    print(f"Sample Radius: {radius_sample}")
    print(f"Calculated Circumference: {circumference_result}")
if __name__ == '__main__':
    main()