def validate_input(values, weights):
    if not isinstance(values, list) or not isinstance(weights, list):
        raise ValueError("Inputs must be lists")
    if len(values) != len(weights):
        raise ValueError("Lists must be of the same length")

def calculate_weighted_sum(values, weights):
    return sum(v * w for v, w in zip(values, weights))

def weighted_average(values, weights):
    validate_input(values, weights)
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be non-zero")
    return calculate_weighted_sum(values, weights) / sum(weights)

if __name__ == '__main__':
    values = [10, 20, 30]
    weights = [1, 2, 3]
    print(weighted_average(values, weights))