WEIGHT_UNIT = 'kg'

def calculate_weight_difference(x, y):
    return abs(x - y)

if __name__ == '__main__':
    weight1 = 80.5
    weight2 = 70.2
    difference = calculate_weight_difference(weight1, weight2)
    print(f"Difference: {difference} {WEIGHT_UNIT}")