def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 78.5
    sample_weight2 = 82.3
    difference = calculate_absolute_difference(sample_weight1, sample_weight2)
    print(difference)