import sys
if __name__ == '__main__':
    try:
        input_data = "5.0"
        radius = float(input_data)
        if radius > 0:
            area = 3.141592653589793 * (radius ** 2)
            print(area)
        else:
            print("Radius must be a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")