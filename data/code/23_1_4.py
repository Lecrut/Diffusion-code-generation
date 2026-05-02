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
        "result": "Greater" if a > b else "Lesser",
        "difference": difference,
        "ratio": ratio
    }
if __name__ == '__main__':
    print(compare_and_report(10, 5))
    print(compare_and_report(3.5, 7.0))
    print(compare_and_report(42, 42))
    print(compare_and_report(-10, 20))
    print(compare_and_report(0.1, 0.2))