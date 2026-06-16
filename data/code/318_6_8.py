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
    rule1 = "greater_than"
    violations1 = checker.check_adjacent_violations(list1, rule1)
    print(f"\nRule: {rule1}")
    if violations1:
        for index, message in violations1:
            print(f"Index {index}: {message}")
    else:
        print("No violations found.")
    list2 = [10, 5, 12, 3]
    print("\nChecking list:", list2)
    rule2 = "greater_than"
    violations2 = checker.check_adjacent_violations(list2, rule2)
    print(f"\nRule: {rule2}")
    if violations2:
        for index, message in violations2:
            print(f"Index {index}: {message}")
    else:
        print("No violations found.")
    list3 = [5, 5, 10, 10]
    print("\nChecking list:", list3)
    rule3 = "equal"
    violations3 = checker.check_adjacent_violations(list3, rule3)
    print(f"\nRule: {rule3}")
    if violations3:
        for index, message in violations3:
            print(f"Index {index}: {message}")
    else:
        print("No violations found.")