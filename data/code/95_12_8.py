def read_and_check_integers(a=50, b=60, c=70):
    def check(n):
        return n > 0 and n % 2 == 0 and n < 100

    results = {
        "inputs": [a, b, c],
        "status": {}
    }

    for idx, val in enumerate([a, b, c], start=1):
        if check(val):
            results["status"][f"input{idx}"] = 'Pass'
        else:
            results["status"][f"input{idx}"] = 'Fail'

    return results

if __name__ == '__main__':
    result = read_and_check_integers()
    print(result)