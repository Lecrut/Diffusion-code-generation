import math

def calculate_side_length(height):
    if height <= 0:
        raise ValueError("Height must be positive")
    return (2 * height) / math.sqrt(3)

def calculate_perimeter(side_length):
    return 3 * side_length

def main():
    height = 8.73
    try:
        side_length = calculate_side_length(height)
        perimeter = calculate_perimeter(side_length)
        print(f"Side Length: {side_length:.2f}")
        print(f"Perimeter: {perimeter:.2f}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()