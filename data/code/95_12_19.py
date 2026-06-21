def validate_input(n):
    return n > 0 and n % 2 == 0 and n < 100

def combine_and_report(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    for val in [a, b, c]:
        if validate_input(val):
            results["status"][str(val)] = True
        else:
            results["status"][str(val)] = False
    return results

if __name__ == '__main__':
    sample_values = combine_and_report(2, 4, 6)
    print(sample_values)