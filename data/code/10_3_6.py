class NameList:
    def __init__(self):
        self.names = ["Alice", "Bob", "Charlie"]

    def get_first(self):
        return self.names[0]

if __name__ == '__main__':
    registry = NameList()
    print(registry.get_first())