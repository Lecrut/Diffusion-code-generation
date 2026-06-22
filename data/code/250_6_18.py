def validate_input(values, weights):
    if not isinstance(values, list) or not isinstance(weights, list):
        raise ValueError("Inputs must be lists")
    if len(values) != len(weights):
        raise ValueError("Values and weights lists must have the same length")
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")

def compute_weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    values = [10, 20, 30]
    weights = [1, 2, 3]
    validate_input(values, weights)
    average = compute_weighted_average(values, weights)
    print(average)