class ActionRepeater:
    def __init__(self):
        self.actions = ["Action 1", "Action 2", "Action 3", "Action 4", "Action 5"]

    def perform(self, index):
        return f"Performing {self.actions[index]}"

if __name__ == '__main__':
    repeater = ActionRepeater()
    results = [repeater.perform(i) for i in range(5)]
    print(results)