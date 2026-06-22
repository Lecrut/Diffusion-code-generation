def compute_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    result = compute_weight_difference(10.5, 7.2)
    print(result)