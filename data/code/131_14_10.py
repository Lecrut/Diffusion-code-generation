from enum import Enum

class State(Enum):
    OFF = 1
    ON = 2

class Transition:
    def __init__(self, event, next_state):
        self.event = event
        self.next_state = next_state

class StateMachine:
    def __init__(self):
        self.transitions = {
            State.OFF: [
                Transition("POWER_ON", State.ON)
            ],
            State.ON: [
                Transition("POWER_OFF", State.OFF),
                Transition("TOGGLE", State.OFF)
            ]
        }
        self.current_state = State.OFF

    def handle_event(self, event):
        for transition in self.transitions[self.current_state]:
            if transition.event == event:
                self.current_state = transition.next_state
                return True
        return False

if __name__ == '__main__':
    machine = StateMachine()
    print("Initial state:", machine.current_state.name)
    machine.handle_event("POWER_ON")
    print("After POWER_ON:", machine.current_state.name)
    machine.handle_event("TOGGLE")
    print("After TOGGLE:", machine.current_state.name)
    machine.handle_event("POWER_OFF")
    print("After POWER_OFF:", machine.current_state.name)