import random
def generate_random_weights():
    weights = []
    for _ in range(10):
        unit = random.choice(["kg", "lbs"])
        if unit == "kg":
            weight = round(random.uniform(50.0, 200.0), 2)
        else:
            weight = round(random.uniform(100.0, 500.0), 2)
        weights.append((weight, unit))
    return weights
if __name__ == '__main__':
    random_measurements = generate_random_weights()
    print("Generated Random Weight Measurements:")
    for weight, unit in random_measurements:
        print(f"Weight: {weight} {unit}")