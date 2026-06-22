class TruthValueManager:
    _VALID_TYPES = (bool,)

    @staticmethod
    def _validate_boolean(value):
        if not isinstance(value, bool):
            raise ValueError("Expected a boolean value")
        return True

    @staticmethod
    def _compute_inversion(flag):
        return not flag

    def get_opposite(self, value):
        self._validate_boolean(value)
        return self._compute_inversion(value)

if __name__ == '__main__':
    manager = TruthValueManager()
    result_true = manager.get_opposite(True)
    result_false = manager.get_opposite(False)
    print(result_true)
    print(result_false)