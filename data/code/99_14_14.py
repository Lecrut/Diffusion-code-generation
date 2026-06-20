def validate_state(state, criteria):
    return all(criterion(state) for criterion in criteria)

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 50}
    criteria = [
        lambda s: s['temperature'] < 40,
        lambda s: s['humidity'] > 20
    ]
    print(validate_state(state, criteria))