class TruthValueManager:
    _MAPPING = {True: False, False: True}

    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self._MAPPING[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    result1 = manager.get_opposite(True)
    result2 = manager.get_opposite(False)
    print(result1)
    print(result2)