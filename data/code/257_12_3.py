import sys
def calculate_difference(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Inputs must be integers.")
        result = calculate_difference(num1, num2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")