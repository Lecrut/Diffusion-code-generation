def find_violations(lst):
    violations = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            violations.append(lst[i])
    return violations

if __name__ == '__main__':
    sample_list = [1.0, 2.5, 3.3, 3.3, 4.8, 4.7, 5.9]
    result = find_violations(sample_list)
    print(result)