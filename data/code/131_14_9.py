from enum import Enum

class State(Enum):
    START = 1
    PROCESSING = 2
    DONE = 3

class StateMachine:

    def __init__(self):
        self.state = State.START

    def process_event(self, event):
        if self.state == State.START and event == 'start':
            self.state = State.PROCESSING
            return 'Processing started'
        elif self.state == State.PROCESSING and event == 'complete':
            self.state = State.DONE
            return 'Processing completed'
        else:
            return 'Invalid event for current state'
if __name__ == '__main__':
    sm = StateMachine()
    print(sm.process_event('start'))
    print(sm.process_event('complete'))
    print(sm.process_event('start'))