def validate_state(state, criteria):
    return all(criteria(state))

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 85}
    criteria = [
        lambda s: s['temperature'] < 40,
        lambda s: s['humidity'] < 90
    ]
    print(validate_state(state, criteria))