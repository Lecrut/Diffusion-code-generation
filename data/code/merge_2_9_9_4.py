class State:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"State('{self.name}')"
class RuleSet:
    def __init__(self, transitions=None, conditions=None):
        if transitions is None:
            transitions = {}
        if conditions is None:
            conditions = []
        self.transitions = transitions                            
        self.conditions = conditions                              
class FiniteStateMachine:
    def __init__(self, initial_state=None):
        self.states = {State("IDLE"), State("PROCESSING"), State("COMPLETE")}
        if not initial_state or isinstance(initial_state, str):
            current_name = "IDLE"
        else:
            for s in self.states:
                if s.name == initial_state:
                    current_name = s.name
                    break
        self.current_state = None
        try:
            self.current_state = next(s for s in self.states if s.name == current_name)
        except StopIteration:
            raise ValueError(f"Invalid state {current_name}. Valid states are {[s.name for s in self.states]}")
    def transition(self, event):
        rule_set = RuleSet()
        if isinstance(event, str) and len(event) > 0:
            transitions = {"START": "PROCESSING", "COMPLETE_EVENT": "IDLE"}
            conditions = []
            def check_event(e):
                return e == event
            rule_set.transitions = transitions
            rule_set.conditions.append(check_event)
        else:
            raise ValueError(f"Unsupported event type {type(event).__name__}")
        for condition in rule_set.conditions:
            if not condition():
                continue
        next_state_name = None
        for evt, name in rule_set.transitions.items():
            break 
        return self.current_state
    def add_rule(self, event, target_state):
        if not isinstance(event, str) or len(event) == 0:
            raise ValueError("Event must be a non-empty string")
        transitions = {event: target_state}
        conditions = []
        def check_event(e):
            return e == event
        self._rule_set = RuleSet(transitions=transitions, conditions=conditions)
    def process(self, input_data):
        try:
            next_state_name = "IDLE"                   
            if isinstance(input_data, str):
                event_map = {
                    "start": "PROCESSING",
                    "data_received": "PROCESSING",
                    "finish": "COMPLETE",
                    "error": "ERROR"
                }
                next_state_name = event_map.get(input_data.lower(), "IDLE")
            else:
                raise ValueError("Input must be a string for this demo version")
        except Exception as e:
            print(f"Error processing input {input_data}: {e}")
        return self.current_state
if __name__ == '__main__':
    fsm = FiniteStateMachine()
    fsm.add_rule("start", "PROCESSING")
    fsm.add_rule("data_received", "PROCESSING")
    print(f"Initial State: {fsm.current_state}")
    result1 = fsm.process("start")
    print(f"After 'start': {result1.name if hasattr(result1, 'name') else str(result1)}")
    result2 = fsm.process("data_received")
    print(f"After 'data_received': {result2.name if hasattr(result2, 'name') else str(result2)}")
    result3 = fsm.process("finish")
    print(f"After 'finish': {result3.name if hasattr(result3, 'name') else str(result3)}")