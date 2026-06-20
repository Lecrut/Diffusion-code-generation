def validate_state(state, criteria):
    return all(criteria(state))

if __name__ == '__main__':
    sample_state = {'temperature': 30, 'humidity': 85}
    sample_criteria = [lambda s: s['temperature'] < 40, lambda s: s['humidity'] < 90]
    print(validate_state(sample_state, sample_criteria))