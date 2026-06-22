def validate_weight(weight):
    if weight < 0:
        raise ValueError("Weights cannot be negative")
    return weight

def compute_weight_difference(weight1, weight2):
    validated_weight1 = validate_weight(weight1)
    validated_weight2 = validate_weight(weight2)
    return abs(validated_weight1 - validated_weight2)

if __name__ == '__main__':
    sample_weights = {
        'object1': 20.3,
        'object2': 15.7
    }
    
    try:
        difference = compute_weight_difference(sample_weights['object1'], sample_weights['object2'])
        print(difference)
    except ValueError as e:
        print(e)