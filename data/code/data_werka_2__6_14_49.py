def compute_weight_difference(weight1, weight2):
    weights = {'weight1': weight1, 'weight2': weight2}
    for name, value in weights.items():
        if value < 0:
            raise ValueError(f"{name} cannot be negative")
    return abs(weight1 - weight2)

if __name__ == '__main__':
    try:
        weight1 = 20.3
        weight2 = 5.8
        difference = compute_weight_difference(weight1, weight2)
        print(difference)
    except ValueError as e:
        print(e)