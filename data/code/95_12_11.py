def validate_number(n):
    if n > 0 and n % 2 == 0 and n < 100:
        return True
    return False

def combine_and_report(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    for i, val in enumerate([a, b, c], start=1):
        if validate_number(val):
            results["status"][f"input{i}"] = 'Pass'
        else:
            results["status"][f"input{i}"] = 'Fail'
    return results

if __name__ == '__main__':
    sample_results = combine_and_report(20, 45, -1)
    print(sample_results)