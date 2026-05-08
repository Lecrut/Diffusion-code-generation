class Validator:
    def combine_and_report(self, a, b, c):
        results = {
            "inputs": [a, b, c],
            "status": {}
        }
        checks = {
            "a": {"positive": a > 0, "even": a % 2 == 0, "magnitude": a < 100},
            "b": {"positive": b > 0, "even": b % 2 == 0, "magnitude": b < 100},
            "c": {"positive": c > 0, "even": c % 2 == 0, "magnitude": c < 100}
        }
        for key, check_data in checks.items():
            results["status"][key] = {
                "positive": check_data["positive"],
                "even": check_data["even"],
                "magnitude": check_data["magnitude"]
            }
        return results
if __name__ == '__main__':
    validator = Validator()
    sample_a = 10
    sample_b = 50
    sample_c = 150
    report = validator.combine_and_report(sample_a, sample_b, sample_c)
    print(report)