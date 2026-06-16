class ListChecker:
    def check_adjacent_violations(self, data, rule_type):
        violations = []
        n = len(data)
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if rule_type == "strictly_increasing" and not (a < b):
                violations.append((i, f"Violation: {a} is not strictly less than {b}"))
            elif rule_type == "non_decreasing" and not (a <= b):
                violations.append((i, f"Violation: {a} is not less than or equal to {b}"))
        return violations
if __name__ == '__main__':
    checker = ListChecker()
    sample_data_1 = [1, 3, 2, 5, 4]
    rule_1 = "strictly_increasing"
    violations_1 = checker.check_adjacent_violations(sample_data_1, rule_1)
    print(f"Data: {sample_data_1}, Rule: {rule_1}")
    if violations_1:
        for index, message in violations_1:
            print(message)
    else:
        print("No violations found.")
    print("-" * 20)
    sample_data_2 = [1, 2, 2, 4, 3]
    rule_2 = "non_decreasing"
    violations_2 = checker.check_adjacent_violations(sample_data_2, rule_2)
    print(f"Data: {sample_data_2}, Rule: {rule_2}")
    if violations_2:
        for index, message in violations_2:
            print(message)
    else:
        print("No violations found.")