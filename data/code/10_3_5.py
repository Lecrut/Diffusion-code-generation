class NameList:
    NAMES = ["Alice", "Bob", "Charlie"]
    @staticmethod
    def get_first():
        return NameList.NAMES[0]
if __name__ == '__main__':
    print(NameList.get_first())