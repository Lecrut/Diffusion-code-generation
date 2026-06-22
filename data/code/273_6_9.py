import time

class ActionExecutor:
    def perform_action(self):
        print('Action executed')

def perform_repeated_actions(action_executor, delay=2, repetitions=5):
    for _ in range(repetitions):
        action_executor.perform_action()
        time.sleep(delay)

if __name__ == '__main__':
    executor = ActionExecutor()
    perform_repeated_actions(executor)