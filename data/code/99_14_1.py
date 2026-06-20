def validate_state(state, criteria):
    for criterion in criteria:
        if not criterion(state):
            return False
    return True

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 50}
    criteria = [
        lambda s: s['temperature'] < 40,
        lambda s: s['humidity'] > 20
    ]
    print(validate_state(state, criteria))