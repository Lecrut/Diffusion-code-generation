class ListChecker:
    def check_adjacent_rule(self, data, rule_type):
        violations = []
        n = len(data)
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if rule_type == "increasing" and not (a <= b):
                violations.append((i, a, b))
            elif rule_type == "decreasing" and not (a >= b):
                violations.append((i, a, b))
        return violations
if __name__ == '__main__':
    checker = ListChecker()
    sample_list = [1, 3, 2, 5, 4]
    increasing_violations = checker.check_adjacent_rule(sample_list, "increasing")
    print("Increasing Violations:")
    if increasing_violations:
        for index, val1, val2 in increasing_violations:
            print(f"Violation at index {index}: {val1} and {val2}")
    else:
        print("No increasing violations found.")
    decreasing_violations = checker.check_adjacent_rule(sample_list, "decreasing")
    print("\nDecreasing Violations:")
    if decreasing_violations:
        for index, val1, val2 in decreasing_violations:
            print(f"Violation at index {index}: {val1} and {val2}")
    else:
        print("No decreasing violations found.")