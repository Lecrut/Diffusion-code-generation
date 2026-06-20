class StateManager:
    START_STATE = 'start'
    STOP_STATE = 'stop'
    RESET_STATE = 'reset'

    def __init__(self):
        self.state = None

    def set_state(self, state):
        if state in (self.START_STATE, self.STOP_STATE, self.RESET_STATE):
            self.state = state
            return True
        return False

    def handle_input(self, input_value):
        if input_value == 'start':
            return self.set_state(self.START_STATE)
        elif input_value == 'stop':
            return self.set_state(self.STOP_STATE)
        elif input_value == 'reset':
            return self.set_state(self.RESET_STATE)
        else:
            raise ValueError('Invalid input')
if __name__ == '__main__':
    manager = StateManager()
    print(manager.handle_input('start'))
    print(manager.handle_input('stop'))
    print(manager.handle_input('reset'))
    try:
        print(manager.handle_input('pause'))
    except ValueError as e:
        print(e)