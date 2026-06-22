class BooleanOrchestrator:
    def __init__(self, data):
        self.data = data
        self.cache = None
        self._is_dirty = True

    def _compute_result(self):
        if not self.data:
            return False
        result = False
        for item in self.data:
            if item:
                result = True
                break
        self.cache = result
        self._is_dirty = False
        return result

    def has_true(self):
        if self._is_dirty:
            return self._compute_result()
        return self.cache

    def get_first_true_index(self):
        if not self.data:
            return -1
        for index, item in enumerate(self.data):
            if item:
                return index
        return -1

    def count_true(self):
        total = 0
        for item in self.data:
            if item:
                total += 1
        return total

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    sample_empty = []
    sample_all_false = [False, False, False]
    
    checker = BooleanOrchestrator(sample_data)
    print(checker.has_true())
    print(checker.get_first_true_index())
    print(checker.count_true())
    
    empty_checker = BooleanOrchestrator(sample_empty)
    print(empty_checker.has_true())
    print(empty_checker.get_first_true_index())
    
    all_false_checker = BooleanOrchestrator(sample_all_false)
    print(all_false_checker.has_true())
    print(all_false_checker.get_first_true_index())
    print(all_false_checker.count_true())