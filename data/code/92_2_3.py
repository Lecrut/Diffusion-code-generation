class TruthValueManager:
    _TRUE_VALUE = True
    _FALSE_VALUE = False

    def get_opposite(self, value):
        if value is True:
            return self._FALSE_VALUE
        if value is False:
            return self._TRUE_VALUE
        raise ValueError("Argument must be a boolean type")

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not True))