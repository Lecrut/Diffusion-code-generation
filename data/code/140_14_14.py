class StateManager:
    def __init__(self):
        self.state = 'stopped'

    def start(self):
        if self.state != 'running':
            self.state = 'running'
            print('State: Running')

    def stop(self):
        if self.state == 'running':
            self.state = 'stopped'
            print('State: Stopped')

    def reset(self):
        self.state = 'stopped'
        print('State: Reset')

if __name__ == '__main__':
    manager = StateManager()
    manager.start()
    manager.stop()
    manager.reset()