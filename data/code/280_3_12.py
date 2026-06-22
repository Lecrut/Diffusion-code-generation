import time

class ActionRepeater:
    DELAY_SECONDS = 1
    
    @staticmethod
    def perform_action(action_string):
        print(action_string)
    
    @classmethod
    def repeat_action(cls, action_string, num_times):
        for _ in range(num_times):
            cls.perform_action(action_string)
            time.sleep(cls.DELAY_SECONDS)

if __name__ == '__main__':
    action = "Hello World"
    count = 5
    ActionRepeater.repeat_action(action, count)