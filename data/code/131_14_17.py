from enum import Enum

class State(Enum):
    START = 1
    A = 2
    B = 3
    C = 4

class StateMachine:

    def __init__(self):
        self.current_state = State.START
        self.transitions = {State.START: {('event1',): State.A, ('event2',): State.B}, State.A: {('event3',): State.C}, State.B: {('event4',): State.C}, State.C: {}}

    def process_event(self, event):
        if self.current_state in self.transitions and (event,) in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][event,]
            return True
        return False
if __name__ == '__main__':
    machine = StateMachine()
    print(machine.process_event('event1'))
    print(machine.process_event('event3'))
    print(machine.process_event('event2'))
    print(machine.process_event('event4'))
    print(machine.current_state)