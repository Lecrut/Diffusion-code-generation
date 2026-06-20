def evaluate_implication(a, b):
    return not a or b

def evaluate_equivalence(a, b):
    return a == b

if __name__ == '__main__':
    sample_values = [(False, False), (False, True), (True, False), (True, True)]
    
    print("Truth Table for Implication (A -> B):")
    for a, b in sample_values:
        result = evaluate_implication(a, b)
        print(f"A: {a}, B: {b}, A -> B: {result}")
    
    print("\nTruth Table for Equivalence (A == B):")
    for a, b in sample_values:
        result = evaluate_equivalence(a, b)
        print(f"A: {a}, B: {b}, A == B: {result}")