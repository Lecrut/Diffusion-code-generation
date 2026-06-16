import random
def validate_choice(choice):
    if choice not in ['A', 'B', 'C']:
        return False
    return True
class FaultTolerantApp:
    def __init__(self, primary_input='X'):
        self.primary_input = primary_input
    def process(self):
        if validate_choice(self.primary_input):
            print(f"Primary input '{self.primary_input}' is valid.")
            result = f"Result based on {self.primary_input}"
        else:
            fallback_inputs = ['A', 'B', 'C']
            self.fallback_index = random.randint(0, 2)
            selected_fallback = fallback_inputs[self.fallback_index]
            print(f"Fallback activated. Selected '{selected_fallback}'.")
            result = f"Result based on {selected_fallback}"
        return result
if __name__ == '__main__':
    app = FaultTolerantApp(primary_input='Z')
    output = app.process()
    print(output)