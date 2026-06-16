import sys
def validate_choice(choice):
    if choice not in ['A', 'B']:
        return False
    return True
class FaultTolerantApp:
    def __init__(self, primary_input='X'):
        self.primary_input = primary_input
        self.fallback_active = False
    def process(self):
        if validate_choice(self.primary_input):
            print(f"Primary choice '{self.primary_input}' is valid.")
        else:
            self.fallback_active = True
            fallback_value = 'B'
            print(f"Fallback mechanism activated. Using value '{fallback_value}'.")
    def run_simulation(self, test_cases=['A', 'X']):
        for case in test_cases:
            app = FaultTolerantApp(case)
            app.process()
if __name__ == '__main__':
    simulator = FaultTolerantApp('X')
    simulator.run_simulation(['A', 'X'])