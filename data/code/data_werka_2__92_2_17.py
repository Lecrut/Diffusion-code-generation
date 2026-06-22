class TruthValueManager:
    _FALSE = False
    _TRUE = True

    def get_opposite(self, value):
        if value is self._TRUE:
            return self._FALSE
        if value is self._FALSE:
            return self._TRUE
        raise ValueError("Value must be a boolean")

if __name__ == '__main__':
    tvm = TruthValueManager()
    print(tvm.get_opposite(True))
    print(tvm.get_opposite(False))