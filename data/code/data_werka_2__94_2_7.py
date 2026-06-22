class BooleanChecker:
    VALID_TYPES = (bool,)
    
    @staticmethod
    def _validate_input(boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for item in boolean_list:
            if not isinstance(item, BooleanChecker.VALID_TYPES):
                raise ValueError(f"Invalid type in list: {type(item)}")
        return boolean_list

    def has_at_least_one_true(self, boolean_list):
        validated_list = self._validate_input(boolean_list)
        return any(validated_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_list = [False, False, True, False]
    result = checker.has_at_least_one_true(sample_list)
    print(result)