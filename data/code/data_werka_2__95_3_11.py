class ValueChecker:
    MIN_VAL = 1
    MAX_VAL = 99
    
    @staticmethod
    def _is_even(n):
        return n % 2 == 0
    
    def check(self, n):
        return n > self.MIN_VAL and self._is_even(n) and n < self.MAX_VAL

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.check(50)
    print(result)