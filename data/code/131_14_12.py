from enum import Enum

class State(Enum):
    INIT = 1
    STATE_A = 2
    STATE_B = 3

class Event(Enum):
    EVENT_X = 1
    EVENT_Y = 2

class StateMachine:

    def __init__(self):
        self.state = State.INIT

    def handle_event(self, event):
        if self.state == State.INIT and event == Event.EVENT_X:
            return self.transition_to(State.STATE_A)
        elif self.state == State.STATE_A and event == Event.EVENT_Y:
            return self.transition_to(State.STATE_B)
        else:
            return None

    def transition_to(self, new_state):
        self.state = new_state
        return f'Transitioned to state: {new_state.name}'
if __name__ == '__main__':
    machine = StateMachine()
    print(machine.handle_event(Event.EVENT_X))
    print(machine.handle_event(Event.EVENT_Y))