def calculate_weight_difference(x, y):
    return abs(x - y)

if __name__ == '__main__':
    weight_a = 80
    weight_b = 45
    difference = calculate_weight_difference(weight_a, weight_b)
    print(f"The weight difference is: {difference}")