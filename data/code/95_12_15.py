def check_integer(n):
    return n > 0 and n % 2 == 0 and n < 100

class Validator:
    def combine_and_report(self, a, b, c):
        results = {
            "inputs": [a, b, c],
            "status": {}
        }
        for key, val in zip(['a', 'b', 'c'], [a, b, c]):
            if check_integer(val):
                results["status"][key] = 'Pass'
            else:
                results["status"][key] = 'Fail'
        return results

if __name__ == '__main__':
    validator = Validator()
    sample_results = validator.combine_and_report(2, 4, 6)
    print(sample_results)