def check_input(n):
    return n > 0 and n % 2 == 0 and n < 100

def combine_and_report(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    for val in [a, b, c]:
        if check_input(val):
            results["status"][str(val)] = 'Pass'
        else:
            results["status"][str(val)] = 'Fail'
    return results

if __name__ == '__main__':
    sample_values = (10, 20, 30)
    result = combine_and_report(*sample_values)
    print(result)