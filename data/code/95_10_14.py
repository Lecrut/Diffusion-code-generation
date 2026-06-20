class Validator:
    def combine_and_report(self, num1, num2, num3):
        results = {}
        for number in [num1, num2, num3]:
            is_positive = number > 0
            is_even = number % 2 == 0
            is_less_than_100 = number < 100
            if is_positive and is_even and is_less_than_100:
                results[number] = "Positive, even, less than 100"
            elif not is_positive:
                results[number] = "Not positive"
            elif not is_even:
                results[number] = "Not even"
            elif not is_less_than_100:
                results[number] = "Not less than 100"
        return results

if __name__ == '__main__':
    validator = Validator()
    test_numbers = [34, -2, 99]
    result = validator.combine_and_report(*test_numbers)
    print(result)