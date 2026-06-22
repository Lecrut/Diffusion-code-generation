import time

class ActionRepeater:
    def __init__(self):
        self.action_count = 0

    def perform_action(self):
        print("Action executed")
        self.action_count += 1

    def repeat_sequence(self, times=10, delay=0.5):
        for _ in range(times):
            self.perform_action()
            time.sleep(delay)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeater.repeat_sequence()
    print(f"Total actions performed: {repeater.action_count}")