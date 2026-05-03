def weight_difference(weights):
    if not weights:
        return 0
    return max(weights) - min(weights)
if __name__ == '__main__':
    sample_weights = [10, 5, 20, 15, 8]
    result = weight_difference(sample_weights)
    print(result)