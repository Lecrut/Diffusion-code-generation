def calculate_weight_difference(weight_one, weight_two):
    return abs(weight_one - weight_two)

if __name__ == '__main__':
    sample_weight_one = 150
    sample_weight_two = 120
    result = calculate_weight_difference(sample_weight_one, sample_weight_two)
    print(result)