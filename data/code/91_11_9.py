class BooleanNegator:
    def __init__(self, initial_state=False):
        self.state = initial_state
    
    def negate(self):
        self.state = not self.state

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.state)  # Output: True
    negator.negate()
    print(negator.state)  # Output: False