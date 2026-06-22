class TruthValueManager:
    def get_opposite(self, value):
        if value is True:
            return False
        if value is False:
            return True
        raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not False))