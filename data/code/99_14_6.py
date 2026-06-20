def validate_state(state):
    criteria = [
        (state['age'] >= 18, "Age is below 18"),
        (state['income'] > 50000, "Income is not above 50000"),
        (state['education'] == 'bachelor', "Education level is not bachelor")
    ]
    for criterion, message in criteria:
        if not criterion:
            return False, message
    return True, "All criteria met"

if __name__ == '__main__':
    state = {
        'age': 25,
        'income': 60000,
        'education': 'bachelor'
    }
    result, message = validate_state(state)
    print(result, message)