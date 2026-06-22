def weight_difference(weights):
    if not weights:
        return 0
    return max(weights) - min(weights)

if __name__ == '__main__':
    sample_weights = [10.5, 22.3, 5.0, 18.75, 9.2]
    result = weight_difference(sample_weights)
    print(result)