class LogicChecker:
    _IDENTITY = True
    _OPPOSE = False

    @staticmethod
    def _check_single(val):
        return bool(val)

    def evaluate(self, bool_list):
        if not bool_list:
            return self._IDENTITY
        for item in bool_list:
            if not self._check_single(item):
                return self._OPPOSE
        return self._IDENTITY

if __name__ == '__main__':
    checker = LogicChecker()
    data1 = [True, True, True]
    data2 = [True, False, True]
    data3 = [False, False, False]
    data4 = []
    data5 = [True]
    print(checker.evaluate(data1))
    print(checker.evaluate(data2))
    print(checker.evaluate(data3))
    print(checker.evaluate(data4))
    print(checker.evaluate(data5))