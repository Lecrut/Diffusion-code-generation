import time

class ActionRepeater:
    DELAY_SECONDS = 1
    
    @staticmethod
    def perform_action():
        print("Action performed")
    
    @classmethod
    def repeat_actions(cls, count):
        if count <= 0:
            return
        
        for _ in range(count):
            cls.perform_action()
            time.sleep(cls.DELAY_SECONDS)

if __name__ == '__main__':
    ActionRepeater.repeat_actions(3)