class TruthValueManager:
    def get_opposite(self, value):
        return not value

if __name__ == '__main__':
    manager = TruthValueManager()
    print(f"Opposite of True is {manager.get_opposite(True)}")
    print(f"Opposite of False is {manager.get_opposite(False)}")