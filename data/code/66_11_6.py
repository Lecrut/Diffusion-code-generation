def find_violations(lst):
    violations = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            violations.append(lst[i])
    return violations

if __name__ == '__main__':
    sample_list = [1.0, 2.5, 3.3, 2.8, 4.0, 5.1]
    result = find_violations(sample_list)
    print(result)