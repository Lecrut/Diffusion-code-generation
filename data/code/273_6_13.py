import time

class ActionRepeater:
    def __init__(self, action):
        self.action = action
    
    def perform_action(self):
        print('Action executed')
    
    def repeat_sequence(self, delay=2, repetitions=5):
        for _ in range(repetitions):
            self.perform_action()
            time.sleep(delay)

if __name__ == '__main__':
    executor = ActionRepeater(print)
    executor.repeat_sequence()