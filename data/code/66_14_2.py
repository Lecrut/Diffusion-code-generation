def find_violations(data):
    violations = []
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            violations.append(data[i])
    return violations
if __name__ == '__main__':
    input_list = [1.0, 2.0, 2.0, 4.0, 5.0, 3.0, 7.0]
    result = find_violations(input_list)
    print(result)