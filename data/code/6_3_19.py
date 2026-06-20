def weight_difference(weights):
    if not weights:
        return 0
    heaviest = weights[0]
    lightest = weights[0]
    for weight in weights[1:]:
        if weight > heaviest:
            heaviest = weight
        elif weight < lightest:
            lightest = weight
    return heaviest - lightest

if __name__ == '__main__':
    sample_weights = [5, 10, 2, 8, 15, 1]
    result = weight_difference(sample_weights)
    print(result)