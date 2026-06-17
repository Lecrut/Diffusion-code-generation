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
                elif a > b:
                    violations.append((i, f"Violation: {a} is not greater than {b}"))
            elif rule_type == "less_than":
                if a > b:
                    violations.append((i, f"Violation: {a} is not less than {b}"))
                elif a < b:
                    violations.append((i, f"Violation: {a} is not less than {b}"))
            elif rule_type == "equal":
                if a != b:
                    violations.append((i, f"Violation: {a} is not equal to {b}"))
            else:
                return []
        return violations
if __name__ == '__main__':
    checker = ListChecker()
    sample_data1 = [1, 5, 3, 8, 2]
    rule1 = "greater_than"
    violations1 = checker.check_adjacent_violations(sample_data1, rule1)
    print(f"Data: {sample_data1}, Rule: {rule1}")
    if violations1:
        for index, message in violations1:
            print(f"{index}: {message}")
    else:
        print("No violations found.")
    print("-" * 20)
    sample_data2 = [10, 5, 12, 3]
    rule2 = "greater_than"
    violations2 = checker.check_adjacent_violations(sample_data2, rule2)
    print(f"Data: {sample_data2}, Rule: {rule2}")
    if violations2:
        for index, message in violations2:
            print(f"{index}: {message}")
    else:
        print("No violations found.")
    print("-" * 20)
    sample_data3 = [5, 5, 5, 5]
    rule3 = "greater_than"
    violations3 = checker.check_adjacent_violations(sample_data3, rule3)
    print(f"Data: {sample_data3}, Rule: {rule3}")
    if violations3:
        for index, message in violations3:
            print(f"{index}: {message}")
    else:
        print("No violations found.")
    print("-" * 20)
    sample_data4 = [10, 8, 5]
    rule4 = "less_than"
    violations4 = checker.check_adjacent_violations(sample_data4, rule4)
    print(f"Data: {sample_data4}, Rule: {rule4}")
    if violations4:
        for index, message in violations4:
            print(f"{index}: {message}")
    else:
        print("No violations found.")
    print("-" * 20)