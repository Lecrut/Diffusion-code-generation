class BooleanInverter:
    def __init__(self):
        self._cache = {}

    def negate(self, flag: bool) -> bool:
        if flag in self._cache:
            return self._cache[flag]
        result = not flag
        self._cache[flag] = result
        return result

if __name__ == '__main__':
    inverter = BooleanInverter()
    true_result = inverter.negate(True)
    false_result = inverter.negate(False)
    print(true_result)
    print(false_result)