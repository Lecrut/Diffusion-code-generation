class TruthValueManager:
    def __init__(self):
        self._truth_map = {True: False, False: True}

    def get_opposite(self, value):
        if type(value) is not bool:
            raise ValueError("Expected boolean input")
        return self._truth_map[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    result_true = manager.get_opposite(True)
    result_false = manager.get_opposite(False)
    print(result_true)
    print(result_false)