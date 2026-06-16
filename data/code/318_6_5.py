class ListChecker:
    def check_adjacent_rule(self, data, rule_type):
        violations = []
        if len(data) < 2:
            return violations
        for i in range(len(data) - 1):
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
    sample_list1 = [1, 5, 3, 8, 2]
    print("--- Checking for 'greater_than' rule ---")
    result1 = checker.check_adjacent_rule(sample_list1, "greater_than")
    for violation in result1:
        print(violation)
    print("\n--- Checking for 'less_than' rule ---")
    result2 = checker.check_adjacent_rule(sample_list1, "less_than")
    for violation in result2:
        print(violation)
    sample_list2 = [10, 5, 12, 3]
    print("\n--- Checking for 'equal' rule ---")
    result3 = checker.check_adjacent_rule(sample_list2, "equal")
    for violation in result3:
        print(violation)