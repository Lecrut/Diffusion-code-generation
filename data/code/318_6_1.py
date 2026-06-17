class ListChecker:
    def check_adjacent_rule(self, data, rule_type):
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
    sample_list1 = [1, 5, 3, 8, 2]
    print("--- Checking for 'greater_than' rule ---")
    violations1 = checker.check_adjacent_rule(sample_list1, "greater_than")
    if violations1:
        for violation in violations1:
            print(violation)
    else:
        print("No violations found.")
    sample_list2 = [10, 5, 12, 3]
    print("\n--- Checking for 'greater_than' rule on second list ---")
    violations2 = checker.check_adjacent_rule(sample_list2, "greater_than")
    if violations2:
        for violation in violations2:
            print(violation)
    else:
        print("No violations found.")
    sample_list3 = [5, 5, 10, 10]
    print("\n--- Checking for 'equal' rule ---")
    violations3 = checker.check_adjacent_rule(sample_list3, "equal")
    if violations3:
        for violation in violations3:
            print(violation)
    else:
        print("No violations found.")