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
    sample_weights = [10, 5, 20, 15, 8]
    result = weight_difference(sample_weights)
    print(result)