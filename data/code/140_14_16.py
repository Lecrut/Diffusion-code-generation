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
            self.state = 'stopped'
            return True
        return False

    def reset(self):
        self.state = 'idle'
        return True
if __name__ == '__main__':
    manager = StateManager()
    commands = ['start', 'start', 'stop', 'reset', 'start']
    for command in commands:
        if command == 'start':
            print(manager.start())
        elif command == 'stop':
            print(manager.stop())
        elif command == 'reset':
            print(manager.reset())