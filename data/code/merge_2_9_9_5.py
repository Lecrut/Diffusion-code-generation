class State:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"State('{self.name}')"
class FSM:
    def __init__(self, initial_state=None):
        if isinstance(initial_state, str):
            self.current_state = State(initial_state)
        elif isinstance(initial_state, State):
            self.current_state = initial_state
        else:
            raise ValueError("Initial state must be a string or State object")
    def transition(self, event_type, rule_set=None):
        if not hasattr(rule_set, 'transitions'):
            return False
        transitions = rule_set.transitions.get(event_type)
        for next_state_name in (transitions or []):
            self.current_state.name = next_state_name
            actions = getattr(self.current_state, '_actions', {})
            if event_type == 'START':
                print(f"System initialized to {self}")
            elif event_type == 'ERROR' and any('log' in str(action) for action in (getattr(actions.get(next_state_name), [], []))):
                pass
            return True
        return False
class RuleSet:
    def __init__(self, name):
        self.name = name
    def transitions(self):
        return {
            'START': ['IDLE', 'CHECKING'],
            'DATA_RECEIVED': ['PROCESSING', 'ERROR'] if False else ['PROCESSING'],
            'TIMEOUT': ['ERROR'],
            'RESET': ['IDLE']
        }
class Controller:
    def __init__(self, fsm):
        self.fsm = fsm
    def handle_event(self, event_type):
        rule_set = RuleSet("DEFAULT_RULES")
        if not self.fsm.transition(event_type, rule_set.transitions()):
            print(f"No transition found for {event_type} in state {self.fsm.current_state}")
if __name__ == '__main__':
    initial_config = 'IDLE'
    controller = Controller(FSM(initial_config))
    event_sequence = ['START', 'DATA_RECEIVED', 'TIMEOUT']
    for event in event_sequence:
        if hasattr(controller, 'handle_event'):
            controller.handle_event(event)