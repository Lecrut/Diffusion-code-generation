class StateManager:
    def __init__(self):
        self.state = 'stopped'

    def is_valid_state_transition(self, new_state):
        valid_transitions = {
            'start': ['stopped'],
            'stop': ['running'],
            'reset': ['running', 'stopped']
        }
        return new_state in valid_transitions and self.state in valid_transitions[new_state]

    def transition_state(self, command):
        if not self.is_valid_state_transition(command):
            raise ValueError("Invalid state transition")
        if command == 'start':
            self.state = 'running'
        elif command == 'stop':
            self.state = 'stopped'
        elif command == 'reset':
            self.state = 'stopped'

if __name__ == '__main__':
    manager = StateManager()
    commands = ['start', 'running', 'stop', 'idle', 'reset']
    for cmd in commands:
        try:
            manager.transition_state(cmd)
            print(f"State transitioned to: {manager.state}")
        except ValueError as e:
            print(e)