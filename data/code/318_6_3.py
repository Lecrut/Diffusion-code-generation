class ListChecker:
    def check_adjacent_violations(self, data, rule_type):
        violations = []
        n = len(data)
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if rule_type == "greater_than":
                if a < b:
                    violations.append((f"Violation at index {i}: {a} is not greater than {b}"))
            elif rule_type == "less_than":
                if a > b:
                    violations.append((f"Violation at index {i}: {a} is not less than {b}"))
            elif rule_type == "equal":
                if a != b:
                    violations.append((f"Violation at index {i}: {a} is not equal to {b}"))
        return violations
if __name__ == '__main__':
    checker = ListChecker()
    sample_list_1 = [1, 5, 3, 8, 2]
    print("--- Checking for 'greater_than' rule ---")
    violations_gt = checker.check_adjacent_violations(sample_list_1, "greater_than")
    if violations_gt:
        for violation in violations_gt:
            print(violation)
    else:
        print("No violations found.")
    sample_list_2 = [10, 5, 12, 3]
    print("\n--- Checking for 'greater_than' rule on second list ---")
    violations_gt_2 = checker.check_adjacent_violations(sample_list_2, "greater_than")
    if violations_gt_2:
        for violation in violations_gt_2:
            print(violation)
    else:
        print("No violations found.")
    sample_list_3 = [5, 5, 10, 10]
    print("\n--- Checking for 'equal' rule ---")
    violations_eq = checker.check_adjacent_violations(sample_list_3, "equal")
    if violations_eq:
        for violation in violations_eq:
            print(violation)
    else:
        print("No violations found.")