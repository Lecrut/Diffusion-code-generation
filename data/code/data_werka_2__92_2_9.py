class TruthValueManager:
    _VALID_TYPES = (bool,)

    @staticmethod
    def _validate_boolean(value):
        if type(value) not in TruthValueManager._VALID_TYPES:
            raise ValueError("Value must be of boolean type")
        return True

    def get_opposite(self, value):
        self._validate_boolean(value)
        return bool(1 - int(value))

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not False))