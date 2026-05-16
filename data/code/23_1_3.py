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
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return {
            "result": "Greater Than",
            "difference": difference,
            "ratio": ratio
        }
    else:
        return {
            "result": "Less Than",
            "difference": abs(difference),
            "ratio": 1.0 / ratio if ratio != 0 else float('inf')
        }
if __name__ == '__main__':
    value1 = 15.5
    value2 = 10.0
    report1 = compare_and_report(value1, value2)
    print(report1)
    value3 = -5
    value4 = 10
    report2 = compare_and_report(value3, value4)
    print(report2)
    value5 = 7.2
    value6 = 7.2
    report3 = compare_and_report(value5, value6)
    print(report3)
    value7 = 20.0
    value8 = 4.0
    report4 = compare_and_report(value7, value8)
    print(report4)