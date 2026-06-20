class BooleanChecker:
    def is_both_true(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = BooleanChecker()
    sample1_a = True
    sample1_b = True
    print(checker.is_both_true(sample1_a, sample1_b))
    
    sample2_a = False
    sample2_b = True
    print(checker.is_both_true(sample2_a, sample2_b))