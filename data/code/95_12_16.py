def check_number(n):
    if n > 0 and n % 2 == 0 and n < 100:
        return True
    else:
        return False

def validate_numbers(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    for key, val in zip("abc", [a, b, c]):
        if check_number(val):
            results["status"][key] = 'Pass'
        else:
            results["status"][key] = 'Fail'
    return results

if __name__ == '__main__':
    sample_results = validate_numbers(20, 45, 80)
    print(sample_results)