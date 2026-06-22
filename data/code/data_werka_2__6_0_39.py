WEIGHT_THRESHOLD = 10.0

def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    sample_weight1 = 95.2
    sample_weight2 = 83.7
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)