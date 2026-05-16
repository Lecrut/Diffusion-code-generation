def compare_and_report(a, b):
    if a == b:
        return {
            "result": "Equal",
            "difference": 0,
            "ratio": 1.0
        }
    if a > b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    difference = larger - smaller
    ratio = larger / smaller
    return {
        "result": "Greater than",
        "difference": difference,
        "ratio": ratio
    } if a > b else {
        "result": "Less than",
        "difference": abs(difference),
        "ratio": 1 / ratio
    }
if __name__ == '__main__':
    value1 = 15.5
    value2 = 8.0
    report1 = compare_and_report(value1, value2)
    print(report1)
    value3 = -5
    value4 = 10
    report2 = compare_and_report(value3, value4)
    print(report2)
    value5 = 3.14159
    value6 = 3.14
    report3 = compare_and_report(value5, value6)
    print(report3)
    value7 = 7
    value8 = 7
    report4 = compare_and_report(value7, value8)
    print(report4)