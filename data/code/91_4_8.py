class BooleanNegator:
    NEGATION_TABLE = {True: False, False: True}

    @staticmethod
    def get_opposite(boolean: bool) -> bool:
        return BooleanNegator.NEGATION_TABLE[boolean]

if __name__ == '__main__':
    sample1 = True
    result1 = BooleanNegator.get_opposite(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    
    sample2 = False
    result2 = BooleanNegator.get_opposite(sample2)
    print(f"Input: {sample2}, Output: {result2}")