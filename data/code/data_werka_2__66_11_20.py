def find_violations(lst):
    violations = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            violations.append(lst[i])
    return violations

if __name__ == '__main__':
    SAMPLE_LIST = [2.0, 3.5, 4.0, 4.0, 5.5, 6.0, 5.8]
    result = find_violations(SAMPLE_LIST)
    print(result)