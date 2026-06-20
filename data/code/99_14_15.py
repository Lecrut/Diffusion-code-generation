def validate_state(state, criteria):
    if not isinstance(state, dict):
        raise ValueError("State must be a dictionary")
    if not all(isinstance(criterion, callable) for criterion in criteria):
        raise ValueError("All criteria must be callable functions")

    return all(criterion(state) for criterion in criteria)

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 50}
    criteria = [
        lambda s: s['temperature'] < 40,
        lambda s: s['humidity'] > 20
    ]
    print(validate_state(state, criteria))