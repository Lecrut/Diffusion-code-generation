class NameList:
    def __init__(self, names):
        self.names = names

    def get_first(self):
        return self.names[0] if self.names else None

if __name__ == '__main__':
    sample_names = ["Elena", "Mark", "Priya", "Omar"]
    roster = NameList(sample_names)
    print(roster.get_first())