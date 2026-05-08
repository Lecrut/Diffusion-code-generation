class StateMachine:
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.initial_state = None
    def add_state(self, state):
        self.states[state] = {}
    def add_transition(self, state, condition, next_state):
        if state not in self.states:
            self.add_state(state)
        self.states[state][condition] = next_state
        self.transitions.setdefault(state, {})[condition] = next_state
    def set_initial_state(self, state):
        self.initial_state = state
    def get_next_state(self, current_state, condition):
        if current_state in self.states and condition in self.states[current_state]:
            return self.states[current_state][condition]
        return None
    def get_state_transitions(self, current_state):
        return self.states.get(current_state, {})
    def get_all_states(self):
        return list(self.states.keys())
if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state("A")
    sm.add_state("B")
    sm.add_state("C")
    sm.add_transition("A", "condition_1", "B")
    sm.add_transition("A", "condition_2", "C")
    sm.add_transition("B", "condition_3", "A")
    sm.add_transition("B", "condition_4", "C")
    sm.add_transition("C", "condition_5", "A")
    sm.set_initial_state("A")
    print("--- State Machine Setup ---")
    print(f"States: {sm.get_all_states()}")
    print(f"Initial State: {sm.initial_state}")
    print("\nTransitions from A:")
    print(sm.get_state_transitions("A"))
    print("\nTransitions from B:")
    print(sm.get_state_transitions("B"))
    print("\nTransitions from C:")
    print(sm.get_state_transitions("C"))
    print("\n--- State Transition Lookups ---")
    current = "A"
    print(f"Current State: {current}")
    condition_to_test = "condition_1"
    next_state = sm.get_next_state(current, condition_to_test)
    print(f"Testing transition from {current} with '{condition_to_test}': {next_state}")
    current = "B"
    condition_to_test = "condition_4"
    next_state = sm.get_next_state(current, condition_to_test)
    print(f"Testing transition from {current} with '{condition_to_test}': {next_state}")
    current = "C"
    condition_to_test = "condition_5"
    next_state = sm.get_next_state(current, condition_to_test)
    print(f"Testing transition from {current} with '{condition_to_test}': {next_state}")
    current = "A"
    condition_to_test = "non_existent_condition"
    next_state = sm.get_next_state(current, condition_to_test)
    print(f"Testing transition from {current} with '{condition_to_test}': {next_state}")