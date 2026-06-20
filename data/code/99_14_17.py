class StateValidator:
    MIN_TEMPERATURE = 20
    MAX_TEMPERATURE = 40
    MIN_HUMIDITY = 30
    MAX_HUMIDITY = 95

    @staticmethod
    def validate_temperature(state):
        return StateValidator.MIN_TEMPERATURE <= state['temperature'] < StateValidator.MAX_TEMPERATURE

    @staticmethod
    def validate_humidity(state):
        return StateValidator.MIN_HUMIDITY <= state['humidity'] < StateValidator.MAX_HUMIDITY

    @classmethod
    def validate_state(cls, state):
        return cls.validate_temperature(state) and cls.validate_humidity(state)

if __name__ == '__main__':
    state = {'temperature': 30, 'humidity': 50}
    validator = StateValidator()
    print(validator.validate_state(state))