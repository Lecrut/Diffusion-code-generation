from enum import Enum

class State(Enum):
    IDLE = 1
    PROCESSING = 2
    COMPLETED = 3

class Event(Enum):
    START = 1
    DATA_RECEIVED = 2
    END = 3
transitions = {(State.IDLE, Event.START): State.PROCESSING, (State.PROCESSING, Event.DATA_RECEIVED): State.PROCESSING, (State.PROCESSING, Event.END): State.COMPLETED}

class StateMachine:

    def __init__(self):
        self.current_state = State.IDLE

    def process_event(self, event):
        new_state = transitions.get((self.current_state, event), None)
        if new_state is not None:
            self.current_state = new_state
            return f'State transitioned from {self.current_state.name} to {new_state.name}'
        else:
            return 'Invalid state transition'
if __name__ == '__main__':
    machine = StateMachine()
    print(machine.process_event(Event.START))
    print(machine.process_event(Event.DATA_RECEIVED))
    print(machine.process_event(Event.END))