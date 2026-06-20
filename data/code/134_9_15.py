class SingleTrueChecker:
    def assert_single_true(self, properties):
        return sum(properties) == 1

if __name__ == '__main__':
    checker = SingleTrueChecker()
    sample_properties = [False, True, False]
    result = checker.assert_single_true(sample_properties)
    print(result)