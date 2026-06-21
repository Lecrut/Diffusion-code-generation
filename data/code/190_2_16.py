class ListChecker:
    def __init__(self, primary_list):
        self.primary_set = set(primary_list)

    def check_element(self, secondary_list):
        return bool(self.primary_set.intersection(secondary_list))

if __name__ == '__main__':
    checker = ListChecker([10, 25, 37, 42, 50])
    sample_secondary = [37, 60, 75]
    result = checker.check_element(sample_secondary)
    print(f"Primary List: {checker.primary_set}")
    print(f"Secondary List: {sample_secondary}")
    print(f"Does any element from the secondary list exist in the primary list? {result}")