from enum import Enum

class State(Enum):
    INIT = 1
    STATE_1 = 2
    STATE_2 = 3
    FINAL = 4

class Event(Enum):
    EVENT_A = 1
    EVENT_B = 2
    EVENT_C = 3

class StateMachine:

    def __init__(self):
        self.state = State.INIT

    def handle_event(self, event):
        if self.state == State.INIT and event == Event.EVENT_A:
            return self.transition_to_state_1()
        elif self.state == State.STATE_1 and event == Event.EVENT_B:
            return self.transition_to_state_2()
        elif self.state == State.STATE_2 and event == Event.EVENT_C:
            return self.transition_to_final()
        else:
            return None

    def transition_to_state_1(self):
        self.state = State.STATE_1
        return State.STATE_1.value

    def transition_to_state_2(self):
        self.state = State.STATE_2
        return State.STATE_2.value

    def transition_to_final(self):
        self.state = State.FINAL
        return State.FINAL.value
if __name__ == '__main__':
    sm = StateMachine()
    print(sm.handle_event(Event.EVENT_A))
    print(sm.handle_event(Event.EVENT_B))
    print(sm.handle_event(Event.EVENT_C))