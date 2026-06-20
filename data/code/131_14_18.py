from enum import Enum

class State(Enum):
    START = 1
    PROCESSING = 2
    DONE = 3

class StateMachine:

    def __init__(self):
        self.state = State.START

    def process_event(self, event):
        if self.state == State.START and event == 'START':
            self.state = State.PROCESSING
            return 'Processing started'
        elif self.state == State.PROCESSING and event == 'END':
            self.state = State.DONE
            return 'Processing done'
        else:
            return 'Invalid event for current state'
if __name__ == '__main__':
    sm = StateMachine()
    print(sm.process_event('START'))
    print(sm.process_event('END'))
    print(sm.process_event('START'))