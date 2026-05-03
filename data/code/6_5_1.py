def weight_difference(weights):
    if not weights:
        return 0
    heaviest = weights[0]
    lightest = weights[0]
    for weight in weights:
        if weight > heaviest:
            heaviest = weight
        if weight < lightest:
            lightest = weight
    return heaviest - lightest
if __name__ == '__main__':
    sample_weights1 = [10, 5, 20, 15]
    result1 = weight_difference(sample_weights1)
    print(result1)
    sample_weights2 = [3, 1, 4, 1, 5, 9, 2, 6]
    result2 = weight_difference(sample_weights2)
    print(result2)
    sample_weights3 = [100]
    result3 = weight_difference(sample_weights3)
    print(result3)
    sample_weights4 = []
    result4 = weight_difference(sample_weights4)
    print(result4)