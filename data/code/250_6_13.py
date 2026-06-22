def calculate_weighted_average(values, weights):
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    
    total = sum(v * w for v, w in zip(values, weights))
    return total / sum(weights)

if __name__ == '__main__':
    values = [45, 60, 75]
    weights = [2, 3, 1]
    result = calculate_weighted_average(values, weights)
    print(result)