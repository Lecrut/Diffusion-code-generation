import sys
def calculate_difference(num1, num2):
    try:
        result = num1 - num2
        return result
    except TypeError:
        return "Error: Invalid input types."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    difference = calculate_difference(num1, num2)
    print(difference)