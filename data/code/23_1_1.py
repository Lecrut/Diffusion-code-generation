def compare_and_report(a, b):
    if a == b:
        return {
            "result": "Equal",
            "difference": 0,
            "ratio": 1.0
        }
    elif a > b:
        larger = a
        smaller = b
        difference = a - b
        ratio = a / b
    else:
        larger = b
        smaller = a
        difference = b - a
        ratio = b / a
    return {
        "result": "Greater" if a > b else "Lesser",
        "difference": abs(a - b),
        "ratio": larger / smaller
    }
if __name__ == '__main__':
    value1 = 15.5
    value2 = 7.0
    report1 = compare_and_report(value1, value2)
    print(report1)
    value3 = -10
    value4 = 5
    report2 = compare_and_report(value3, value4)
    print(report2)
    value5 = 3.14159
    value6 = 3.14
    report3 = compare_and_report(value5, value6)
    print(report3)