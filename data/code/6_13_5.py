import sys
def calculate_weight_difference(weight1, weight2):
    try:
        diff = abs(weight1 - weight2)
        print(f"The simple weight difference is: {diff}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")
if __name__ == '__main__':
    sample_weight1 = 105.5
    sample_weight2 = 98.75
    try:
        weight1 = float(sample_weight1)
        weight2 = float(sample_weight2)
        calculate_weight_difference(weight1, weight2)
    except ValueError:
        print("Error: Sample inputs could not be converted to numbers.")