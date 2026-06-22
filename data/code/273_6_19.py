import time

def perform_action():
    print('Task completed')

def execute_sequence(action_func):
    for _ in range(5):
        action_func()
        time.sleep(2)

if __name__ == '__main__':
    sample_task = perform_action
    execute_sequence(sample_task)