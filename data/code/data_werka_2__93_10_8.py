class BooleanChecker:
    FALSE_VALUE = False

    def are_both_false(self, first, second):
        if first is not self.FALSE_VALUE:
            return False
        if second is not self.FALSE_VALUE:
            return False
        return True

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))