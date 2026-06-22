DIVISOR_LABELS = {
    1: "unity",
    2: "even_prime",
    10: "decimal_base",
    100: "century"
}

def find_all_positive_divisors(target):
    if not isinstance(target, int) or target < 1:
        return []
    found = set()
    bound = int(target**0.5)
    index = 1
    while index <= bound:
        remainder = target % index
        if remainder == 0:
            found.add(index)
            paired = target // index
            found.add(paired)
        index += 1
    return sorted(found)

def categorize_divisor(digit, labels):
    key = digit if digit in labels else 0
    if key == 0:
        if digit % 2 == 0:
            return "even"
        if digit == 1:
            return "unity"
        return "other"
    return labels[key]

def print_divisor_details(number):
    divisors = find_all_positive_divisors(number)
    details = []
    for d in divisors:
        label = categorize_divisor(d, DIVISOR_LABELS)
        details.append(f"{d} ({label})")
    return details

if __name__ == '__main__':
    sample_number = 100
    computed_details = print_divisor_details(sample_number)
    for entry in computed_details:
        print(entry)