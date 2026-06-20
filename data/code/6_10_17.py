def weight_difference(weights):
    if not weights:
        return 0
    return max(weights) - min(weights)

if __name__ == '__main__':
    sample_weights = [72.5, 68.3, 81.2, 55.0, 90.1, 77.8, 63.4]
    print(weight_difference(sample_weights))