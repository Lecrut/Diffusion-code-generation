from enum import Enum

class State(Enum):
    STATE_A = 1
    STATE_B = 2
    STATE_C = 3

class StateMachine:
    def __init__(self):
        self.current_state = State.STATE_A

    def transition(self, event):
        if self.current_state == State.STATE_A and event == 'event1':
            self.current_state = State.STATE_B
        elif self.current_state == State.STATE_B and event == 'event2':
            self.current_state = State.STATE_C
        elif self.current_state == State.STATE_C and event == 'event3':
            self.current_state = State.STATE_A

    def get_current_state(self):
        return self.current_state

if __name__ == '__main__':
    sm = StateMachine()
    sm.transition('event1')
    print(sm.get_current_state())
    sm.transition('event2')
    print(sm.get_current_state())
    sm.transition('event3')
    print(sm.get_current_state())