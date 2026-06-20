def validate_number(n, name):
    return n > 0 and n % 2 == 0 and n < 100

def combine_and_report(a, b, c):
    results = {
        "inputs": [a, b, c],
        "status": {}
    }
    for val, name in zip([a, b, c], ['a', 'b', 'c']):
        if validate_number(val, name):
            results["status"][name] = {"positive": True, "even": True, "magnitude": True}
        else:
            results["status"][name] = {"positive": False, "even": False, "magnitude": False}
    return results

if __name__ == '__main__':
    sample_values = combine_and_report(2, 4, 6)
    print(sample_values)