def is_temperature_valid(state):
    return state['temperature'] < 40

def is_humidity_valid(state):
    return state['humidity'] > 20

def validate_state(state, criteria):
    for criterion in criteria:
        if not criterion(state):
            return False
    return True

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 50}
    criteria = [is_temperature_valid, is_humidity_valid]
    print(validate_state(state, criteria))