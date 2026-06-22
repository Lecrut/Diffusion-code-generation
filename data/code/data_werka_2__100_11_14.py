class BooleanUniformityChecker:
    UNIFORM_TRUE = "all_true"
    UNIFORM_FALSE = "all_false"
    MIXED = "mixed"
    EMPTY = "empty"

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        for item in data:
            if not isinstance(item, bool):
                raise ValueError("All elements must be boolean values")
        return True

    @staticmethod
    def determine_uniformity(data):
        BooleanUniformityChecker._validate_input(data)
        
        if len(data) == 0:
            return BooleanUniformityChecker.EMPTY
        
        if all(data):
            return BooleanUniformityChecker.UNIFORM_TRUE
        
        if not any(data):
            return BooleanUniformityChecker.UNIFORM_FALSE
            
        return BooleanUniformityChecker.MIXED

if __name__ == '__main__':
    true_list = [True, True, True]
    false_list = [False, False, False]
    mixed_list = [True, False, True]
    empty_list = []
    
    print(BooleanUniformityChecker.determine_uniformity(true_list))
    print(BooleanUniformityChecker.determine_uniformity(false_list))
    print(BooleanUniformityChecker.determine_uniformity(mixed_list))
    print(BooleanUniformityChecker.determine_uniformity(empty_list))