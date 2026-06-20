class LogicSystem:
    def check_condition(self, x, y):
        return x and y

if __name__ == '__main__':
    system = LogicSystem()
    print(system.check_condition(5, 3))
    print(system.check_condition(10, 10))
    print(system.check_condition(2, 7))
    print(system.check_condition(0, -5))