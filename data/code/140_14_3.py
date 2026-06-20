class StateManager:

    def __init__(self):
        self.state = 'idle'

    def start(self):
        if self.state == 'idle':
            self.state = 'running'
            return True
        return False

    def stop(self):
        if self.state == 'running':
            self.state = 'idle'
            return True
        return False

    def reset(self):
        self.state = 'idle'
        return True
if __name__ == '__main__':
    manager = StateManager()
    print(manager.start())
    print(manager.stop())
    print(manager.reset())
    print(manager.start())