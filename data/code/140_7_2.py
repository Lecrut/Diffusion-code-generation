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
    def get_state_info(self, state):
        return self.states.get(state, {})
    def get_all_states(self):
        return list(self.states.keys())
if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state("S0")
    sm.add_state("S1")
    sm.add_state("S2")
    sm.add_transition("S0", "condition_A", "S1")
    sm.add_transition("S0", "condition_B", "S2")
    sm.add_transition("S1", "condition_C", "S0")
    sm.add_transition("S1", "condition_D", "S2")
    sm.add_transition("S2", "condition_A", "S0")
    sm.set_initial_state("S0")
    print("--- State Machine Data Structure ---")
    print("States:", sm.get_all_states())
    print("Initial State:", sm.initial_state)
    print("\nTransitions:")
    for state in sm.get_all_states():
        print(f"From {state}: {sm.get_state_info(state)}")
    print("\n--- State Transitions (Lookups) ---")
    test_state = "S0"
    print(f"Current State: {test_state}")
    print(f"Transition on condition_A: {sm.get_next_state(test_state, 'condition_A')}")
    print(f"Transition on condition_X (non-existent): {sm.get_next_state(test_state, 'condition_X')}")
    test_state = "S1"
    print(f"\nCurrent State: {test_state}")
    print(f"Transition on condition_C: {sm.get_next_state(test_state, 'condition_C')}")
    print(f"Transition on condition_D: {sm.get_next_state(test_state, 'condition_D')}")
    test_state = "S2"
    print(f"\nCurrent State: {test_state}")
    print(f"Transition on condition_A: {sm.get_next_state(test_state, 'condition_A')}")
    print(f"Transition on condition_Z (non-existent): {sm.get_next_state(test_state, 'condition_Z')}")