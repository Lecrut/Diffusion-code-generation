from enum import Enum

class State(Enum):
    STATE_A = 1
    STATE_B = 2
    STATE_C = 3

class Transition:

    def __init__(self, from_state, event, to_state):
        self.from_state = from_state
        self.event = event
        self.to_state = to_state

class StateMachine:

    def __init__(self):
        self.transitions = []

    def add_transition(self, transition: Transition):
        self.transitions.append(transition)

    def get_next_state(self, current_state: State, event) -> State:
        for transition in self.transitions:
            if transition.from_state == current_state and transition.event == event:
                return transition.to_state
        raise ValueError(f'No transition defined from {current_state} with event {event}')
if __name__ == '__main__':
    machine = StateMachine()
    machine.add_transition(Transition(State.STATE_A, 'e1', State.STATE_B))
    machine.add_transition(Transition(State.STATE_B, 'e2', State.STATE_C))
    machine.add_transition(Transition(State.STATE_C, 'e3', State.STATE_A))
    try:
        current_state = State.STATE_A
        print(f'Starting state: {current_state.name}')
        events = ['e1', 'e2', 'e3']
        for event in events:
            current_state = machine.get_next_state(current_state, event)
            print(f"After event '{event}', new state: {current_state.name}")
    except ValueError as e:
        print(e)