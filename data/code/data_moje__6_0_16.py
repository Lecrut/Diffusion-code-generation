def calculate_weight_difference(weight1, weight2):
    diff = weight1 - weight2
    return diff if diff >= 0 else -diff

if __name__ == '__main__':
    sample_weight1 = 150.5
    sample_weight2 = 142.8
    result = calculate_weight_difference(sample_weight1, sample_weight2)
    print(result)