class Repeater:
    def __init__(self):
        self.counter = 0

    def repeat(self):
        while self.counter < 100:
            self.counter += 1
            print(f"Repeat {self.counter} times")

if __name__ == '__main__':
    repeater_instance = Repeater()
    repeater_instance.repeat()