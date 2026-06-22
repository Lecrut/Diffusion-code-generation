def find_out_of_range_weights(weights, low=50, high=200):
    return [w for w in weights if w < low or w > high]

if __name__ == '__main__':
    sample_weights = [45, 50, 120, 200, 205, 75, 99, 210, 5, 150]
    outliers = find_out_of_range_weights(sample_weights)
    print(outliers)