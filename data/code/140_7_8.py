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
        if current_state in self.states:
            return self.states[current_state]
        return {}
    def get_all_states(self):
        return list(self.states.keys())
if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state("S0")
    sm.add_state("S1")
    sm.add_state("S2")
    sm.add_state("S3")
    sm.add_transition("S0", "condition_A", "S1")
    sm.add_transition("S0", "condition_B", "S2")
    sm.add_transition("S1", "condition_C", "S3")
    sm.add_transition("S2", "condition_A", "S1")
    sm.add_transition("S2", "condition_B", "S3")
    sm.add_transition("S3", "condition_C", "S0")
    sm.set_initial_state("S0")
    print("--- State Machine Setup Complete ---")
    print("States:", sm.get_all_states())
    print("Initial State:", sm.initial_state)
    print("\n--- Testing Transitions ---")
    current = "S0"
    print(f"Start at {current}")
    condition1 = "condition_A"
    next_state1 = sm.get_next_state(current, condition1)
    print(f"From {current} with {condition1}: {next_state1}")
    current = next_state1
    condition2 = "condition_C"
    next_state2 = sm.get_next_state(current, condition2)
    print(f"From {current} with {condition2}: {next_state2}")
    current = next_state2
    condition3 = "condition_C"
    next_state3 = sm.get_next_state(current, condition3)
    print(f"From {current} with {condition3}: {next_state3}")
    current = next_state3
    current = "S0"
    condition4 = "condition_B"
    next_state4 = sm.get_next_state(current, condition4)
    print(f"From {current} with {condition4}: {next_state4}")
    current = next_state4
    current = "S2"
    condition5 = "condition_A"
    next_state5 = sm.get_next_state(current, condition5)
    print(f"From {current} with {condition5}: {next_state5}")
    current = next_state5
    current = "S2"
    condition6 = "condition_B"
    next_state6 = sm.get_next_state(current, condition6)
    print(f"From {current} with {condition6}: {next_state6}")
    current = next_state6
    current = "S0"
    condition7 = "condition_C"
    next_state7 = sm.get_next_state(current, condition7)
    print(f"From {current} with {condition7} (No transition): {next_state7}")