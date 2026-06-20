class LogicSystem:
    def check_condition(self, x, y):
        return x and y

if __name__ == '__main__':
    logic = LogicSystem()
    print(logic.check_condition(True, True))
    print(logic.check_condition(True, False))
    print(logic.check_condition(False, True))
    print(logic.check_condition(False, False))