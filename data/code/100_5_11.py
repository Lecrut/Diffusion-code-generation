class LogicSystem:
    def check_condition(self, x, y):
        return x and y

if __name__ == '__main__':
    system = LogicSystem()
    print(system.check_condition(True, True))
    print(system.check_condition(False, False))
    print(system.check_condition(True, False))
    print(system.check_condition(False, True))