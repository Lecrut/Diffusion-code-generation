import sys

def weight_difference(weights):
    if not weights:
        raise ValueError("List must not be empty")
    min_w = weights[0]
    max_w = weights[0]
    for w in weights[1:]:
        if w < min_w:
            min_w = w
        if w > max_w:
            max_w = w
    return max_w - min_w

if __name__ == '__main__':
    sample_weights = [10, 25, 3, 42, 18, 9, 30]
    result = weight_difference(sample_weights)
    print(result)