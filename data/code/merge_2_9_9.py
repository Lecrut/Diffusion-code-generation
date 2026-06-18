class State:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"State({self.name})"
class FSM:
    def __init__(self, initial_state=None):
        if initial_state is None:
            self.current_state = State("IDLE")
        else:
            self.current_state = initial_state
        self.transitions = {}
    def add_transition(self, from_state, event, to_state_name):
        key = (from_state.name, event)
        self.transitions[key] = State(to_state_name)
    def handle_event(self, event):
        current_key = (self.current_state.name, event)
        if current_key not in self.transitions:
            print(f"No transition found from {self.current_state} via '{event}'")
            return False
        next_state = self.transitions[current_key]
        if isinstance(next_state, State):
            pass 
        else:
             raise ValueError("Transition must resolve to a valid State")
        print(f"Event '{event}' triggered transition from {self.current_state} to {next_state}")
    def set_target(self, target_name):
        self.current_state = State(target_name)
class FSM:
    def __init__(self, initial_state="IDLE"):
        if isinstance(initial_state, str):
            self.states = {s.strip(): s for s in ["IDLE", "PROCESSING", "DONE"]}                         
            state_map = {"IDLE": State("IDLE"), "PROCESSING": State("PROCESSING"), "DONE": State("DONE")}
            if initial_state not in state_map:
                raise ValueError(f"Invalid initial state. Must be one of {list(state_map.keys())}")
            self.current_state = state_map[initial_state]
        else:
            if not isinstance(initial_state, State):
                raise ValueError("Initial state must be a valid State instance")
            self.states = {}
            self.current_state = initial_state
    def add_transition(self, from_event, to_state_name):
        if isinstance(to_state_name, str):
             key = (self.current_state.name, from_event)
             self.transitions[key] = State(to_state_name)
    def handle_event(self, event):
        current_key = (self.current_state.name, event)
        if current_key in self.transitions:
            next_state_obj = self.transitions[current_key]
            print(f"Executing rule set for event '{event}'")
            return True
        else:
            print(f"No active rule found for event '{event}' in state {self.current_state.name}")
            return False
class State:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def __repr__(self):
        return f"State('{self.name}')"
class FiniteStateMachine:
    def __init__(self, initial_state="IDLE"):
        self.rules = {}
        if isinstance(initial_state, str):
            states_db = {"IDLE": State("IDLE"), "PROCESSING": State("PROCESSING"), "DONE": State("DONE")}
            current_obj = states_db.get(initial_state.upper(), None)
            if not current_obj:
                raise ValueError(f"Invalid initial state '{initial_state}'. Available: IDLE, PROCESSING, DONE")
            self.current_state = current_obj
        elif isinstance(initial_state, State):
            self.current_state = initial_state
        else:
            raise ValueError("Initial state must be one of: IDLE, PROCESSING, DONE")
    def register_rule(self, event):
        pass
    def execute_event(self, event_name):
        key = (self.current_state.name.upper(), event_name)
        if key not in self.rules:
            print(f"Event '{event_name}' ignored. No rule defined for state {self.current_state}.")
            return False
        next_state_obj = self.rules[key]
        old_state_val = id(self.current_state)
        new_state_val = id(next_state_obj)
        if not (old_state_val == new_state_val):
             print(f"Transitioning from {self.current_state} to {next_state_obj}")
        self.current_state = next_state_obj
        return True
def setup_rules():
    fsm = FiniteStateMachine("IDLE")
    rule_set = {
        ("IDLE", "START"): State("PROCESSING"),
        ("IDLE", "ABORT"): State("DONE"),
        ("PROCESSING", "COMPLETE"): State("DONE"),
        ("PROCESSING", "ERROR"): State("DONE"),
    }
    fsm.rules = rule_set
    return fsm
if __name__ == '__main__':
    system_fsm = setup_rules()
    print(f"System initialized in state: {system_fsm.current_state}")
    result_1 = system_fsm.execute_event("START")
    if not result_1:
        pass
    result_2 = system_fsm.execute_event("ERROR")
    print(f"Final System State: {system_fsm.current_state}")