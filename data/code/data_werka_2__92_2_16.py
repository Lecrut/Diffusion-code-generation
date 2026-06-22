class TruthValueManager:
    TRUE_CONSTANT = True
    FALSE_CONSTANT = False

    @staticmethod
    def _compute_opposite(val):
        if val is TruthValueManager.TRUE_CONSTANT:
            return TruthValueManager.FALSE_CONSTANT
        if val is TruthValueManager.FALSE_CONSTANT:
            return TruthValueManager.TRUE_CONSTANT
        raise ValueError("Input must be a boolean")

    def get_opposite(self, value):
        return self._compute_opposite(value)

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not True))