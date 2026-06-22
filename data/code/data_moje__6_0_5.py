def calculate_weight_difference(weight1, weight2):
    if weight1 > weight2:
        return weight1 - weight2
    return weight2 - weight1

if __name__ == '__main__':
    sample_weight1 = 10.5
    sample_weight2 = 7.2
    result = calculate_weight_difference(sample_weight1, sample_weight2)
    print(result)