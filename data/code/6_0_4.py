import sys
def calculate_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    weight1 = 150.5
    weight2 = 200.7
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        print("Error: Both inputs must be numeric values.")
        sys.exit(1)
    difference = calculate_difference(weight1, weight2)
    print(difference)