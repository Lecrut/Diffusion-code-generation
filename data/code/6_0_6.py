import sys
def calculate_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    weight1 = 10.5
    weight2 = 5.2
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        print("Error: Both inputs must be numbers.")
        sys.exit(1)
    difference = calculate_difference(weight1, weight2)
    print(difference)