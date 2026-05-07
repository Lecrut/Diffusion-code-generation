class TruthValueManager:
    def get_opposite(self, value):
        return not value
if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))