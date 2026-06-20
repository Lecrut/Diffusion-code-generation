class StateValidator:
    def __init__(self, state):
        self.state = state

    def validate(self, criteria):
        return all(criterion(self.state) for criterion in criteria)

if __name__ == '__main__':
    validator = StateValidator({'temperature': 30, 'humidity': 50})
    criteria = [
        lambda s: s['temperature'] < 40,
        lambda s: s['humidity'] > 20
    ]
    print(validator.validate(criteria))