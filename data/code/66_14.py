def find_violations(data):
    violations = []
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            violations.append(data[i])
    return violations
if __name__ == '__main__':
    input_list = [1.0, 2.5, 3.0, 3.0, 5.1, 6.0, 6.0, 7.5]
    result = find_violations(input_list)
    print(result)