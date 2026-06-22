class NameList:
    def __init__(self, data):
        self.names = list(data)

    def get_first(self):
        return self.names[0] if self.names else None

    def get_count(self):
        return len(self.names)

if __name__ == '__main__':
    names_instance = NameList(["Alice", "Bob", "Charlie"])
    print(names_instance.get_first())
    print(names_instance.get_count())