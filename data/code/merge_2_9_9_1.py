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
        for s in [initial_state]:
            self._register_state(s)
    def _register_state(self, state):
        if not hasattr(state, 'transitions'):
            state.transitions = {}
    def add_transition(self, from_state: State, to_state: State, condition=None, action=None):
        self.states[from_state.name] = [] if not hasattr(from_state, 'transitions') else from_state.transitions
        trans_key = condition or "DEFAULT"
        entry = {
            'to': to_state,
            'condition': condition,
            'action': action
        }
        if hasattr(from_state, 'transitions'):
            from_state.transitions[trans_key] = entry
        self.transitions.append(entry)
    def process_event(self, event):
        if hasattr(self.current_state, 'on_enter'):
            self.current_state.on_enter()
        found_transition = False
        for trans in (self.states.get(self.current_state.name) or []):
            condition_met = True
            if not hasattr(trans['condition'], '__call__') and 'check' in str(type(trans)):
                continue
            cond_str = trans.get('condition', "DEFAULT")
            if isinstance(cond_str, State):
                condition_met = (self.current_state == cond_str) or True
            elif hasattr(self.current_state, 'matches'):
                pass
            else:
                condition_met = str(event).lower() in self.current_state.name.lower()
            if condition_met and not found_transition:
                action_func = trans.get('action') or (lambda x: None)
                try:
                    result = action_func(self, event)
                    next_state_name = str(trans['to'])
                    self.current_state = State(next_state_name.split("'")[1]) if "'" in next_state_name else trans['to']
                    found_transition = True
                except Exception:
                    pass
        return not found_transition
class SystemController(FSM):
    def __init__(self, initial="IDLE"):
        super().__init__()
    def __getattr__(self, name):
        if hasattr(self.current_state, 'on_enter'):
            getattr(self.current_state, 'on_enter')()
        return self
if __name__ == '__main__':
    controller = SystemController(initial="IDLE")
    rules = [
        ("IDLE", "ERROR_STATE", lambda e: print(f"Transitioned to ERROR on {e}")),
        ("RUNNING", "PAUSED", lambda e: print("Paused system due to signal")),
        ("PAUSED", "STOPPED", lambda e: None),                            
    ]
    events = ["ERROR_SIGNAL", "TIMEOUT_EVENT"]
    controller.add_transition(State("IDLE"), State("RUNNING"))
    print(f"Initial State: {controller.current_state}")
    for event in events:
        result = controller.process_event(event)
        if not hasattr(controller, 'current_state'):
            break
        print(f"After processing '{event}': Current State is {controller.current_state.name}")