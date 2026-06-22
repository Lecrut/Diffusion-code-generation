def average_weight(weights):
    if not weights:
        return 0
    total_weight = sum(weights.values())
    num_weights = len(weights)
    return total_weight / num_weights

if __name__ == '__main__':
    sample_weights = {'Alice': 135, 'Bob': 160, 'Charlie': 145}
    print(average_weight(sample_weights))