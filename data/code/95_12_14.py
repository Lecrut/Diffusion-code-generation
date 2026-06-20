def check_number(num):
    return num > 0 and num % 2 == 0 and num < 100

def combine_and_report(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    for val in [a, b, c]:
        status = {}
        if check_number(val):
            status["positivity"] = True
            status["evenness"] = True
            status["magnitude"] = True
        else:
            status["positivity"] = False
            status["evenness"] = False
            status["magnitude"] = False
        results["status"][val] = status
    return results

if __name__ == '__main__':
    sample_values = [2, 4, 6]
    result = combine_and_report(*sample_values)
    print(result)