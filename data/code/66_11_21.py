def detect_order_violations(numbers):
    violations = []
    previous_number = numbers[0]
    for current_number in numbers[1:]:
        if current_number < previous_number:
            violations.append(current_number)
        previous_number = current_number
    return violations

if __name__ == '__main__':
    sample_sequence = [0.5, 1.2, 1.8, 1.8, 2.4, 2.3, 3.0]
    result = detect_order_violations(sample_sequence)
    print(result)