import array

class BooleanOrchestrator:
    def __init__(self, data):
        self._data = data

    def check(self):
        if not self._data:
            return False
        return any(self._data)

    def check_array(self):
        if not self._data:
            return False
        arr = array.array('b', self._data)
        for val in arr:
            if val:
                return True
        return False

    def count_true(self):
        total = 0
        for val in self._data:
            if val:
                total += 1
        return total

if __name__ == '__main__':
    sample_list = [False, False, True, False, False]
    sample_all_false = [False, False, False]
    sample_empty = []

    obj1 = BooleanOrchestrator(sample_list)
    obj2 = BooleanOrchestrator(sample_all_false)
    obj3 = BooleanOrchestrator(sample_empty)

    print(obj1.check())
    print(obj2.check())
    print(obj3.check())
    print(obj1.check_array())
    print(obj1.count_true())