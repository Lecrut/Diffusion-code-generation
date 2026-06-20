def validate_state(state, criteria):
    return all(criterion(state) for criterion in criteria)

if __name__ == '__main__':
    state = {'temperature': 28, 'humidity': 60}
    criteria = [
        lambda s: s['temperature'] < 35,
        lambda s: s['humidity'] > 45
    ]
    print(validate_state(state, criteria))