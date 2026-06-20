class EqualityChecker:
    def are_equal(self, var1, var2):
        if type(var1) != type(var2):
            return False
        if isinstance(var1, (int, float, str)):
            return var1 == var2
        if isinstance(var1, list):
            if len(var1) != len(var2):
                return False
            for v1, v2 in zip(var1, var2):
                if not self.are_equal(v1, v2):
                    return False
            return True
        if isinstance(var1, dict):
            if len(var1) != len(var2):
                return False
            for key in var1:
                if key not in var2 or not self.are_equal(var1[key], var2[key]):
                    return False

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_equal(5, 5))
    print(checker.are_equal(5, 6))
    print(checker.are_equal('hello', 'hello'))
    print(checker.are_equal('hello', 'world'))