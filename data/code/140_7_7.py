class StateMachine:
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.initial_state = None
    def add_state(self, state):
        self.states[state] = {}
    def add_transition(self, from_state, condition, to_state):
        if from_state not in self.states:
            self.add_state(from_state)
        if to_state not in self.states:
            self.add_state(to_state)
        if from_state not in self.states[from_state]:
            self.states[from_state][condition] = {}
        self.states[from_state][condition][from_state] = to_state
    def set_initial_state(self, state):
        self.initial_state = state
    def get_next_state(self, current_state, condition):
        if current_state in self.states and condition in self.states[current_state]:
            return self.states[current_state][condition].get(current_state)
        return None
    def get_state_details(self, state):
        return self.states.get(state, {})
if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state("Start")
    sm.add_state("Running")
    sm.add_state("Stopped")
    sm.set_initial_state("Start")
    sm.add_transition("Start", "ConditionA", "Running")
    sm.add_transition("Running", "ConditionB", "Stopped")
    sm.add_transition("Running", "ConditionC", "Running")
    sm.add_transition("Stopped", "ConditionA", "Start")
    print("--- State Machine Analysis ---")
    print("\nState Details:")
    print(f"Start: {sm.get_state_details('Start')}")
    print(f"Running: {sm.get_state_details('Running')}")
    print(f"Stopped: {sm.get_state_details('Stopped')}")
    print("\nTransitions:")
    print("From Start:")
    print(f"  ConditionA -> Running: {sm.get_next_state('Start', 'ConditionA')}")
    print("From Running:")
    print(f"  ConditionB -> Stopped: {sm.get_next_state('Running', 'ConditionB')}")
    print(f"  ConditionC -> Running: {sm.get_next_state('Running', 'ConditionC')}")
    print("From Stopped:")
    print(f"  ConditionA -> Start: {sm.get_next_state('Stopped', 'ConditionA')}")
    print("\nTesting State Transitions:")
    current = "Start"
    print(f"Initial State: {current}")
    transition1 = sm.get_next_state(current, "ConditionA")
    print(f"Transition from {current} with ConditionA: {transition1}")
    current = transition1
    transition2 = sm.get_next_state(current, "ConditionC")
    print(f"Transition from {current} with ConditionC: {transition2}")
    current = transition2
    transition3 = sm.get_next_state(current, "ConditionB")
    print(f"Transition from {current} with ConditionB: {transition3}")
    current = transition3
    transition4 = sm.get_next_state(current, "ConditionA")
    print(f"Transition from {current} with ConditionA: {transition4}")
    current = transition4
    print(f"\nFinal State reached: {current}")