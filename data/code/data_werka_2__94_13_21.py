class SequenceChecker:
    TRUE_RESULT = True
    FALSE_RESULT = False
    DEFAULT_THRESHOLD = 1

    @staticmethod
    def _validate_predicate(predicate):
        if predicate is None:
            raise ValueError("Predicate cannot be None")
        if not callable(predicate):
            raise ValueError("Predicate must be callable")
        return predicate

    @staticmethod
    def _evaluate_item(item, predicate):
        return predicate(item)

    def check_any(self, sequence, predicate=None):
        if predicate is None:
            predicate = lambda x: bool(x)
        else:
            predicate = self._validate_predicate(predicate)
        
        for item in sequence:
            if self._evaluate_item(item, predicate):
                return self.TRUE_RESULT
        return self.FALSE_RESULT

if __name__ == '__main__':
    checker = SequenceChecker()
    data = [0, False, None, [], {}, 42]
    result = checker.check_any(data, lambda x: x)
    print(result)