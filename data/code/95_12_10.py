def validate_input(value):
    return value > 0 and value % 2 == 0 and value < 100

def combine_and_report(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    checks = ["a", "b", "c"]
    for key in checks:
        val = globals()[key]
        if validate_input(val):
            results["status"][key] = "Pass"
        else:
            results["status"][key] = "Fail"
    return results

if __name__ == '__main__':
    a, b, c = 2, 4, 6
    sample_result = combine_and_report(a, b, c)
    print(sample_result)