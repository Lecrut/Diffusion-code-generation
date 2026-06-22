def weight_difference(weights):
    if not weights:
        return 0
    heaviest = weights[0]
    lightest = weights[0]
    for w in weights:
        if w > heaviest:
            heaviest = w
        if w < lightest:
            lightest = w
    return heaviest - lightest

if __name__ == '__main__':
    sample_weights = [10, 4, 7, 2, 9, 15]
    result = weight_difference(sample_weights)
    print(result)