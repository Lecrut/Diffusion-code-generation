class TruthValueManager:
    _LOOKUP = {True: False, False: True}

    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self._LOOKUP[value]

if __name__ == '__main__':
    mgr = TruthValueManager()
    result_true = mgr.get_opposite(True)
    result_false = mgr.get_opposite(False)
    print(result_true)
    print(result_false)