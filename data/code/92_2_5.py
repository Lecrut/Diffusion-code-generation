class TruthValueManager:
    _VALID_TYPES = (bool,)

    @staticmethod
    def _validate_input(value):
        if type(value) not in TruthValueManager._VALID_TYPES:
            raise ValueError("Expected a boolean type")
        return True

    def get_opposite(self, value):
        TruthValueManager._validate_input(value)
        return value ^ True

if __name__ == '__main__':
    manager = TruthValueManager()
    result_true = manager.get_opposite(True)
    result_false = manager.get_opposite(False)
    print(result_true)
    print(result_false)