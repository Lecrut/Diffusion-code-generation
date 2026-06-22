def compute_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    person1_weight = 85.2
    person2_weight = 79.8
    weight_diff = compute_weight_difference(person1_weight, person2_weight)
    print(f"The weight difference is: {weight_diff}")