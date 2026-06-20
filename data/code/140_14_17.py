class StateManager:

    def __init__(self):
        self.state = 'stopped'

    def start(self):
        if self.state != 'running':
            self.state = 'running'
            return True
        return False

    def stop(self):
        if self.state == 'running':
            self.state = 'stopped'
            return True
        return False

    def reset(self):
        self.state = 'stopped'
        return True
if __name__ == '__main__':
    manager = StateManager()
    print(manager.start())
    print(manager.stop())
    print(manager.reset())
    print(manager.start())