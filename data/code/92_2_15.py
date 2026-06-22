class TruthValueManager:
    def get_opposite(self, value):
        if type(value) is not bool:
            raise ValueError("Input must be a boolean")
        return False if value else True

if __name__ == '__main__':
    manager = TruthValueManager()
    result_true = manager.get_opposite(True)
    result_false = manager.get_opposite(False)
    print(result_true)
    print(result_false)