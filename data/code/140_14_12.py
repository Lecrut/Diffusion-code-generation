class StateManager:
    def __init__(self):
        self.state = 'stop'

    def start(self):
        if self.state != 'start':
            self.state = 'start'
            print('State changed to start')

    def stop(self):
        if self.state != 'stop':
            self.state = 'stop'
            print('State changed to stop')

    def reset(self):
        if self.state != 'reset':
            self.state = 'reset'
            print('State changed to reset')

if __name__ == '__main__':
    manager = StateManager()
    manager.start()
    manager.stop()
    manager.reset()