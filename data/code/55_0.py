import sys
def calculate_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    try:
        a = 3
        b = 4
        c = 5
        perimeter = calculate_perimeter(a, b, c)
        print(perimeter)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")