import time

def perform_action(action_id):
    print(f"Action {action_id} executed")

action_map = {
    '1': perform_action,
    '2': perform_action,
    '3': perform_action,
    '4': perform_action,
    '5': perform_action,
    '6': perform_action,
    '7': perform_action,
    '8': perform_action,
    '9': perform_action,
    '10': perform_action
}

def repeat_sequence():
    for i in range(1, 11):
        action_map[str(i)](i)
        time.sleep(0.5)

if __name__ == '__main__':
    repeat_sequence()