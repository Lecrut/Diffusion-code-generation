def validate_state(state, criteria):
    return all(criteria(state))

if __name__ == '__main__':
    state = {'temperature': 25, 'humidity': 60}
    criteria = [
        lambda s: s['temperature'] < 30,
        lambda s: s['humidity'] > 40
    ]
    result = validate_state(state, criteria)
    print(result)