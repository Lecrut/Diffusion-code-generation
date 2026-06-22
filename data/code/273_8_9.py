import time

class ActionRepeater:
    DELAY_SECONDS = 1
    
    @staticmethod
    def execute_action():
        print('Action executed')
    
    @classmethod
    def repeat_sequence(cls):
        for _ in range(3):
            cls.execute_action()
            time.sleep(cls.DELAY_SECONDS)

if __name__ == '__main__':
    ActionRepeater.repeat_sequence()