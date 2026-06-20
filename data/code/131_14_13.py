from enum import Enum

class State(Enum):
    START = 1
    PROCESSING = 2
    COMPLETED = 3

class StateMachine:

    def __init__(self):
        self.state = State.START

    def process_event(self, event):
        if self.state == State.START and event == 'BEGIN':
            self.state = State.PROCESSING
            return 'Processing started'
        elif self.state == State.PROCESSING and event == 'END':
            self.state = State.COMPLETED
            return 'Processing completed'
        else:
            return 'Invalid event for current state'
if __name__ == '__main__':
    machine = StateMachine()
    print(machine.process_event('BEGIN'))
    print(machine.process_event('END'))
    print(machine.process_event('BEGIN'))