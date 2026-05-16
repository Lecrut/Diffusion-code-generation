import sys
def calculate_average(temp1, temp2):
    try:
        avg = (temp1 + temp2) / 2
        return avg
    except TypeError:
        return "Error: One or both inputs are not valid numbers."
    except Exception:
        return "An unexpected error occurred during calculation."
if __name__ == '__main__':
    temp1_str = "25.5"
    temp2_str = "30.5"
    try:
        temp1 = float(temp1_str)
        temp2 = float(temp2_str)
        result = calculate_average(temp1, temp2)
        print(result)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs can be converted to numbers.")