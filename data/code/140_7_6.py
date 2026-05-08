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
    sm.add_state("A")
    sm.add_state("B")
    sm.add_state("C")
    sm.add_transition("A", "condition_1", "B")
    sm.add_transition("A", "condition_2", "C")
    sm.add_transition("B", "condition_3", "A")
    sm.add_transition("B", "condition_4", "C")
    sm.add_transition("C", "condition_5", "A")
    sm.set_initial_state("A")
    print("--- State Machine Data Structure ---")
    print("States:", sm.get_all_states())
    print("Transitions:", sm.transitions)
    print("\n--- State Transition Analysis ---")
    current = "A"
    print(f"Starting State: {current}")
    condition = "condition_1"
    next_state = sm.get_next_state(current, condition)
    print(f"From {current} with condition '{condition}': Next state is {next_state}")
    condition = "condition_2"
    next_state = sm.get_next_state(current, condition)
    print(f"From {current} with condition '{condition}': Next state is {next_state}")
    current = "B"
    condition = "condition_3"
    next_state = sm.get_next_state(current, condition)
    print(f"From {current} with condition '{condition}': Next state is {next_state}")
    condition = "non_existent_condition"
    next_state = sm.get_next_state(current, condition)
    print(f"From {current} with condition '{condition}': Next state is {next_state}")
    print("\nAll States:")
    print(sm.get_all_states())