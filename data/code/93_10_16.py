class BooleanChecker:
    EXPECTED_TYPES = (bool,)

    def are_both_false(self, val1, val2):
        if type(val1) not in self.EXPECTED_TYPES:
            raise ValueError("val1 must be a boolean")
        if type(val2) not in self.EXPECTED_TYPES:
            raise ValueError("val2 must be a boolean")
        
        return val1 is False and val2 is False

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)