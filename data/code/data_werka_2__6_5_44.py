def compute_weight_difference(x, y):
    return abs(x - y)

if __name__ == '__main__':
    weight_a = 85
    weight_b = 90
    difference = compute_weight_difference(weight_a, weight_b)
    print(f"The weight difference is: {difference} kg")