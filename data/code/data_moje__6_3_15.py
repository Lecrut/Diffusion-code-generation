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
    weights_list = [10, 5, 20, 8, 15]
    result = weight_difference(weights_list)
    print(result)