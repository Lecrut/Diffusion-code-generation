def validate_temperature(state):
    return state['temperature'] < 40

def validate_humidity(state):
    return state['humidity'] > 20

def validate_state(state, criteria):
    for criterion in criteria:
        if not criterion(state):
            return False
    return True

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 50}
    criteria = [validate_temperature, validate_humidity]
    print(validate_state(state, criteria))