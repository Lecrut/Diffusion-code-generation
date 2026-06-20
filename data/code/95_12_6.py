def validate_integer(value):
    return value > 0 and value % 2 == 0 and value < 100

class Validator:
    def combine_and_report(self, a, b, c):
        results = {
            "inputs": [a, b, c],
            "status": {}
        }
        for val in [a, b, c]:
            status = {}
            if validate_integer(val):
                status["positivity"] = True
                status["evenness"] = True
                status["magnitude"] = True
            else:
                status["positivity"] = False
                status["evenness"] = False
                status["magnitude"] = False
            results["status"][str(val)] = status
        return results

if __name__ == '__main__':
    validator = Validator()
    sample_values = [2, 4, 8]
    result = validator.combine_and_report(*sample_values)
    print(result)