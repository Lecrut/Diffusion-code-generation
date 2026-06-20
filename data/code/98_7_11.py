class SystemStateChecker:
    def __init__(self):
        self.state = 0

    def set_flag(self, flag, value):
        if value:
            self.state |= 1 << flag

    def get_state(self):
        return self.state

if __name__ == '__main__':
    checker = SystemStateChecker()
    checker.set_flag(0, True)
    checker.set_flag(1, False)
    checker.set_flag(2, True)
    checker.set_flag(3, True)
    result = checker.get_state()
    print(result)