def validate_states(states, criteria):
    return all(criteria(state) for state in states)

if __name__ == '__main__':
    states = [True, False, True]
    criteria = lambda x: not x
    print(validate_states(states, criteria))