class Validator:
    def combine_and_report(self, a, b, c):
        results = {}
        for num in [a, b, c]:
            is_positive = num > 0
            is_even = num % 2 == 0
            is_less_than_100 = num < 100
            if not is_positive:
                status = "not positive"
            elif not is_even:
                status = "not even"
            elif not is_less_than_100:
                status = "not less than 100"
            else:
                status = "positive, even, and less than 100"
            results[num] = status
        return results

if __name__ == '__main__':
    validator = Validator()
    print(validator.combine_and_report(10, 50, 200))