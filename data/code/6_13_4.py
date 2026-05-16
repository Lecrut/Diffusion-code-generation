import sys
def calculate_weight_difference(weight1, weight2):
    try:
        diff = abs(weight1 - weight2)
        print(f"The simple weight difference is: {diff}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")
if __name__ == '__main__':
    weight1_input = "10.5"
    weight2_input = "25.75"
    try:
        weight1 = float(weight1_input)
        weight2 = float(weight2_input)
        calculate_weight_difference(weight1, weight2)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are numerical values.")