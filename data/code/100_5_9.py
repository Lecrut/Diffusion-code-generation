class LogicSystem:
    @staticmethod
    def check_condition(x, y):
        return x and y

if __name__ == '__main__':
    print(LogicSystem.check_condition(True, True))
    print(LogicSystem.check_condition(False, True))
    print(LogicSystem.check_condition(True, False))
    print(LogicSystem.check_condition(False, False))