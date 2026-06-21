class TruthValueManager:
    _TRUE = True
    _FALSE = False

    def get_opposite(self, value):
        if value is self._TRUE:
            return self._FALSE
        if value is self._FALSE:
            return self._TRUE
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not True))