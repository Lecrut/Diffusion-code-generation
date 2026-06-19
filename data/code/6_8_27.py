def calculate_weight_difference(weight1, weight2):
    return abs(float(weight1) - float(weight2))

if __name__ == '__main__':
    sample_weight1 = 75.5
    sample_weight2 = 68.3
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)