def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return length * width

def main():
    length = 10
    width = 5
    area = calculate_rectangle_area(length, width)
    print(area)

if __name__ == '__main__':
    main()