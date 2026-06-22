class TruthValueManager:
    _OPPOSITE_MAP = (False, True)

    def get_opposite(self, value):
        if value is not False and value is not True:
            raise ValueError("Input must be a boolean")
        return self._OPPOSITE_MAP[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not True))