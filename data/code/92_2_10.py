class TruthValueManager:
    _LOOKUP = {True: False, False: True}

    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Expected boolean input")
        return self._LOOKUP[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))