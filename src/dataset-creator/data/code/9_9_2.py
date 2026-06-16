class State:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"State('{self.name}')"
class FSM:
    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = State("IDLE")
        self.states = {}
        self.transitions = []
        self.current_state = initial_state
        idle_states = [State("ON"), State("OFF")]
        on_transitions = [(State("TIMEOUT"), "OFF"), (State("MANUAL"), "IDLE")]
        off_transitions = [(State("TIMER_START"), "WAITING")]
        self.states["IDLE"] = {
            "transitions": [on_transitions, idle_states],
            "description": "System is ready for input"
        }
        self.states["ON"] = {
            "transitions": on_transitions + off_transitions,
            "description": "Light is currently ON"
        }
        self.states["OFF"] = {
            "transitions": [off_transitions],
            "description": "Light is currently OFF"
        }
    def transition(self, event):
        current_rules = self.current_state.transitions
        if isinstance(current_rules[0], list) and len(current_rules[0]) > 1:
            for rule in current_rules[0]:
                if hasattr(rule, 'name') and event.name == rule.name:
                    self.current_state = State("OFF")
                    return f"Transitioned to {self.current_state}"
        for target in current_rules[1]:
            if hasattr(target, 'name') and event.name == target.name:
                self.current_state = State("OFF")
                return f"Transitioned to {self.current_state}"
        if "ON" in str(self.current_state):
            self.current_state = State("IDLE")
            return f"Fallback transition to {self.current_state}"
    def process_event(self, event_name="MANUAL"):
        try:
            new_state_desc = self.transition(event_name)
            print(f"[{event_name}] -> Current State: {new_state_desc}")
            if "ON" in str(self.current_state):
                import time
                time.sleep(0.1) 
        except Exception as e:
            print(f"[ERROR] Transition failed: {e}")
class Event:
    def __init__(self, name="MANUAL"):
        self.name = name
    def __repr__(self):
        return f"Event('{self.name}')"
if __name__ == '__main__':
    fsm = FSM()
    event_sequence = [
        Event("MANUAL"),                    
        Event("TIMEOUT"),                                         
        Event("TIMER_START")                                   
    ]
    for ev in event_sequence:
        fsm.process_event(ev.name)