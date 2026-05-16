class StateMachine:
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.initial_state = None
    def add_state(self, state_name):
        if state_name not in self.states:
            self.states[state_name] = {}
            self.transitions[state_name] = {}
    def add_transition(self, current_state, input_condition, next_state):
        if current_state in self.states and next_state in self.states:
            if current_state not in self.transitions:
                self.transitions[current_state] = {}
            self.transitions[current_state][input_condition] = next_state
        else:
            raise ValueError("Invalid state names provided.")
    def set_initial_state(self, state_name):
        if state_name in self.states:
            self.initial_state = state_name
        else:
            raise ValueError("Initial state not found.")
    def get_next_state(self, current_state, input_condition):
        if current_state in self.transitions and input_condition in self.transitions[current_state]:
            return self.transitions[current_state][input_condition]
        return None
    def get_current_state(self):
        return self.initial_state
    def run_simulation(self, start_state, sequence_of_inputs):
        if start_state not in self.states:
            return "Error: Start state not defined."
        current_state = start_state
        history = [current_state]
        for input_condition in sequence_of_inputs:
            next_state = self.get_next_state(current_state, input_condition)
            if next_state is None:
                history.append(f"Error: No transition found from {current_state} with input {input_condition}")
                break
            current_state = next_state
            history.append(current_state)
        return history
if __name__ == '__main__':
    sm = StateMachine()
    sm.add_state("Idle")
    sm.add_state("Running")
    sm.add_state("Stopped")
    sm.add_transition("Idle", "Start", "Running")
    sm.add_transition("Running", "Stop", "Stopped")
    sm.add_transition("Stopped", "Start", "Idle")
    sm.set_initial_state("Idle")
    print("--- State Machine Initialization Complete ---")
    simulation_sequence_1 = ["Start", "Stop", "Start"]
    result_1 = sm.run_simulation("Idle", simulation_sequence_1)
    print("\nSimulation 1:")
    print(f"Sequence: {simulation_sequence_1}")
    print(f"Path: {result_1}")
    simulation_sequence_2 = ["Start", "Stop", "Start", "Stop"]
    result_2 = sm.run_simulation("Idle", simulation_sequence_2)
    print("\nSimulation 2:")
    print(f"Sequence: {simulation_sequence_2}")
    print(f"Path: {result_2}")
    simulation_sequence_3 = ["Start", "InvalidInput"]
    result_3 = sm.run_simulation("Idle", simulation_sequence_3)
    print("\nSimulation 3 (Error Test):")
    print(f"Sequence: {simulation_sequence_3}")
    print(f"Path: {result_3}")