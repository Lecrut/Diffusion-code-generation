import sys
def calculate_area(length, width):
    try:
        area = float(length) * float(width)
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area}")
    except ValueError:
        print("Error: Invalid numerical input provided.")
if __name__ == '__main__':
    sample_length = 10.5
    sample_width = 4.2
    calculate_area(sample_length, sample_width)