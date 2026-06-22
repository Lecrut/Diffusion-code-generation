import time

class ActionRepeater:
    def __init__(self):
        self.action_count = 0
    
    def execute_action(self):
        print("Action executed")
        self.action_count += 1
    
    def repeat_sequence(self, times=10):
        for _ in range(times):
            self.execute_action()
            time.sleep(0.5)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeater.repeat_sequence()
    print(f"Total actions executed: {repeater.action_count}")