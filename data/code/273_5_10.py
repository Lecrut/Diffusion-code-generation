class Repeater:
    def __init__(self, action):
        self.action = action

    def repeat(self, n):
        if n <= 0:
            return
        self.action()
        self.repeat(n - 1)

if __name__ == '__main__':
    repeater_instance = Repeater(lambda: print("Action repeated"))
    repeater_instance.repeat(3)