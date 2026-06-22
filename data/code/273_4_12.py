import time

class ActionRepeater:
    def perform_action(self):
        print("Action performed")

def repeat_sequence(action_obj, action_method, count=10, delay=0.5):
    for _ in range(count):
        action_obj.action_method()
        time.sleep(delay)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeat_sequence(repeater, 'perform_action')