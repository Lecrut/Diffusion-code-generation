import sys
def calculate_weight_difference(weight1, weight2):
    try:
        diff = abs(weight1 - weight2)
        return diff
    except TypeError:
        return "Error: Inputs must be numerical."
if __name__ == '__main__':
    weight_a = 10.5
    weight_b = 22.3
    result = calculate_weight_difference(weight_a, weight_b)
    print(result)