NUM_THRESHOLD = 100
MIN_VALUE = 0

def evaluate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    
    positive = value > MIN_VALUE
    even = value % 2 == 0
    within_range = value < NUM_THRESHOLD
    
    if positive and even and within_range:
        return "Positive, even, and less than 100"
    
    reasons = []
    if not positive:
        reasons.append("not positive")
    if not even:
        reasons.append("odd")
    if not within_range:
        reasons.append("greater than or equal to 100")
        
    return "Number is " + ", ".join(reasons)

if __name__ == '__main__':
    test_cases = [42, -5, 7, 100, 105]
    for num in test_cases:
        print(evaluate_number(num))