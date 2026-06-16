class ListChecker:
    def check_adjacent_violations(self, data, rule_type):
        violations = []
        n = len(data)
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if rule_type == "greater_than":
                if a < b:
                    violations.append((i, f"Violation: {a} is not greater than {b}"))
            elif rule_type == "less_than":
                if a > b:
                    violations.append((i, f"Violation: {a} is not less than {b}"))
            elif rule_type == "equal":
                if a != b:
                    violations.append((i, f"Violation: {a} is not equal to {b}"))
        return violations
if __name__ == '__main__':
    checker = ListChecker()
    list1 = [1, 5, 3, 8, 2]
    print("Checking list:", list1)
    violations_gt = checker.check_adjacent_violations(list1, "greater_than")
    print("\nViolations for 'greater_than' rule:")
    if violations_gt:
        for index, message in violations_gt:
            print(f"Index {index}: {message}")
    else:
        print("No violations found.")
    list2 = [10, 5, 8, 3]
    print("\nChecking list:", list2)
    violations_lt = checker.check_adjacent_violations(list2, "less_than")
    print("\nViolations for 'less_than' rule:")
    if violations_lt:
        for index, message in violations_lt:
            print(f"Index {index}: {message}")
    else:
        print("No violations found.")
    list3 = [4, 4, 5, 5]
    print("\nChecking list:", list3)
    violations_eq = checker.check_adjacent_violations(list3, "equal")
    print("\nViolations for 'equal' rule:")
    if violations_eq:
        for index, message in violations_eq:
            print(f"Index {index}: {message}")
    else:
        print("No violations found.")