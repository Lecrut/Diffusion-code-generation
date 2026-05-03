def weight_difference(weights):
    if not weights:
        return 0
    minimum = weights[0]
    maximum = weights[0]
    for weight in weights:
        if weight < minimum:
            minimum = weight
        if weight > maximum:
            maximum = weight
    return maximum - minimum
if __name__ == '__main__':
    sample_weights = [10, 5, 20, 15, 8]
    result = weight_difference(sample_weights)
    print(result)