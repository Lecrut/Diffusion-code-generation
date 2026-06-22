import time

def execute_action(action_name):
    actions = {
        'print': lambda: print(f'Action {action_name} executed'),
        'sleep': lambda: time.sleep(2)
    }
    if action_name in actions:
        actions[action_name]()

def repeat_sequence():
    for _ in range(5):
        execute_action('print')
        execute_action('sleep')

if __name__ == '__main__':
    repeat_sequence()