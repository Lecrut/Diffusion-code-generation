class NegationLogic:
    def __init__(self, flag: bool):
        if type(flag) is not bool:
            raise ValueError("Expected boolean type")
        self.flag = flag

    def get_opposite(self) -> bool:
        return not self.flag

    def flip(self):
        self.flag = not self.flag
        return self.flag

if __name__ == '__main__':
    logic = NegationLogic(True)
    print(logic.get_opposite())
    logic.flip()
    print(logic.get_opposite())
    print(logic.flip())