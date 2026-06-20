class StateManager:
    STATE_STOPPED = 'stopped'
    STATE_RUNNING = 'running'

    def __init__(self):
        self.state = self.STATE_STOPPED

    def start(self):
        if self.state == self.STATE_STOPPED:
            self.state = self.STATE_RUNNING
            return True
        return False

    def stop(self):
        if self.state == self.STATE_RUNNING:
            self.state = self.STATE_STOPPED
            return True
        return False

    def reset(self):
        self.state = self.STATE_STOPPED
        return True
if __name__ == '__main__':
    manager = StateManager()
    print(manager.start())
    print(manager.stop())
    print(manager.reset())