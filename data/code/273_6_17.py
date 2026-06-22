import time

class ActionRepeater:
    def __init__(self):
        self.action = "Action executed"

    def perform_action(self):
        print(self.action)

def repeat_sequence(action_executor, delay=2, repetitions=5):
    for _ in range(repetitions):
        action_executor.perform_action()
        time.sleep(delay)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeat_sequence(repeater)