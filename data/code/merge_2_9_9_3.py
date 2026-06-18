class State:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"State('{self.name}')"
class FSMController:
    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = State("IDLE")
        self.current_state = initial_state
        self.transitions = {
            ("IDLE", "START"): "RUNNING",
            ("IDLE", "STOP"): None,                               
            ("RUNNING", "COMPLETE"): "FINISHED",
            ("RUNNING", "ERROR"): "FAULTED",
            ("RUNNING", "PAUSE"): "SUSPENDED",
            ("SUSPENDED", "RESUME"): "RUNNING",
            ("SUSPENDED", "STOP"): "IDLE",
            ("FINISHED", "RESTART"): "RUNNING",
        }
    def process_event(self, event):
        current_name = self.current_state.name
        matched_rule = None
        for (from_s, from_e), to_s in self.transitions.items():
            if from_s == current_name and from_e == event:
                matched_rule = to_s
                break
        if matched_rule is not None:
            next_state_obj = State(matched_rule)
            print(f"Event '{event}' processed. Transitioning {self.current_state.name} -> {matched_rule}")
            self._update_state(next_state_obj, event)
        else:
            print(f"No transition rule found for Event '{event}' in State '{current_name}'.")
    def _update_state(self, next_state, event):
        old_ref_id = id(self.current_state)
        self.current_state = next_state
    def get_status(self):
        return f"Current State: {self.current_state.name}"
if __name__ == '__main__':
    system_controller = FSMController()
    event_sequence = ["START", "PAUSE", "RESUME", "COMPLETE"]
    print("=== System Control Simulation ===")
    for event in event_sequence:
        system_controller.process_event(event)
        status = system_controller.get_status()
        print(status)