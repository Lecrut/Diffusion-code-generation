class StateMachine:
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.initial_state = None
    def add_state(self, state_name):
        self.states[state_name] = True
    def add_transition(self, current_state, condition, next_state):
        if current_state not in self.states:
            raise ValueError(f"State {current_state} does not exist.")
        if next_state not in self.states:
            raise ValueError(f"State {next_state} does not exist.")
        transition_key = (current_state, condition)
        if transition_key not in self.transitions:
            self.transitions[transition_key] = next_state
    def set_initial_state(self, state_name):
        if state_name in self.states:
            self.initial_state = state_name
        else:
            raise ValueError(f"Initial state {state_name} does not exist.")
    def get_next_state(self, current_state, condition):
        transition_key = (current_state, condition)
        if transition_key in self.transitions:
            return self.transitions[transition_key]
        return None
    def get_current_state(self):
        return self.initial_state
if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state("START")
    sm.add_state("WAITING")
    sm.add_state("RUNNING")
    sm.add_state("STOPPED")
    sm.set_initial_state("START")
    sm.add_transition("START", "condition_A", "WAITING")
    sm.add_transition("WAITING", "condition_B", "RUNNING")
    sm.add_transition("RUNNING", "condition_C", "STOPPED")
    sm.add_transition("STOPPED", "condition_A", "WAITING")
    print("--- State Machine Initialization Complete ---")
    current = sm.get_current_state()
    print(f"Initial State: {current}")
    print("\n--- Simulation ---")
    print(f"Current State: {current}")
    next_state = sm.get_next_state(current, "condition_A")
    print(f"Transition from {current} with condition_A leads to: {next_state}")
    if next_state:
        current = next_state
        print(f"New State: {current}")
    print(f"Current State: {current}")
    next_state = sm.get_next_state(current, "condition_B")
    print(f"Transition from {current} with condition_B leads to: {next_state}")
    if next_state:
        current = next_state
        print(f"New State: {current}")
    print(f"Current State: {current}")
    next_state = sm.get_next_state(current, "condition_C")
    print(f"Transition from {current} with condition_C leads to: {next_state}")
    if next_state:
        current = next_state
        print(f"New State: {current}")
    print(f"Current State: {current}")
    next_state = sm.get_next_state(current, "condition_A")
    print(f"Transition from {current} with condition_A leads to: {next_state}")
    if next_state:
        current = next_state
        print(f"New State: {current}")
    print("\n--- Final State ---")
    print(f"Final State: {current}")
    print("\n--- Testing Invalid Transition ---")
    invalid_next = sm.get_next_state("WAITING", "condition_C")
    print(f"Attempted transition from WAITING with condition_C leads to: {invalid_next}")