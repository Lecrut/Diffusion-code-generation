def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 70.5
    sample_weight2 = 68.2
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)