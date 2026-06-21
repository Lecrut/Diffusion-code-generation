class ListChecker:
    def __init__(self, primary_list):
        self.primary_set = set(primary_list)

    def contains_any(self, secondary_list):
        return bool(self.primary_set.intersection(secondary_list))

if __name__ == '__main__':
    checker = ListChecker([10, 25, 37, 42, 50])
    sample_secondary_list = [37, 60, 65]
    result = checker.contains_any(sample_secondary_list)
    print(f"Primary List: {[10, 25, 37, 42, 50]}")
    print(f"Secondary List: {sample_secondary_list}")
    print(f"Does the primary list contain any elements from the secondary list? {result}")