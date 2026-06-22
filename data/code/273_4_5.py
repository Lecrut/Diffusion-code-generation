import time

class ActionRepeater:
    def __init__(self):
        self.action_count = 0

    def execute_action(self):
        print(f"Action {self.action_count + 1} executed")
        self.action_count += 1

def repeat_sequence(action_func, repetitions=10, delay=0.5):
    for _ in range(repetitions):
        action_func()
        time.sleep(delay)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeat_sequence(repeater.execute_action)
    print(f"Total actions executed: {repeater.action_count}")