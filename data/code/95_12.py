class Validator:
    def combine_and_report(self, a, b, c):
        results = {
            "inputs": [a, b, c],
            "status": {}
        }
        for val in [a, b, c]:
            status = {}
            if val > 0:
                status["positivity"] = True
            else:
                status["positivity"] = False
            if val % 2 == 0:
                status["evenness"] = True
            else:
                status["evenness"] = False
            if val < 100:
                status["magnitude"] = True
            else:
                status["magnitude"] = False
            results["status"][val] = status
        return results
if __name__ == '__main__':
    validator = Validator()
    sample_a = 10
    sample_b = 25
    sample_c = 150
    report = validator.combine_and_report(sample_a, sample_b, sample_c)
    print(report)