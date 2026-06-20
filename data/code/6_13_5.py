def calculate_weight_difference(weight_one, weight_two):
    return weight_one - weight_two

if __name__ == '__main__':
    weight_one = 150.5
    weight_two = 120.25
    difference = calculate_weight_difference(weight_one, weight_two)
    print(difference)