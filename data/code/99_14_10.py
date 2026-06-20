def validate_state(state, criteria):
    return all(criteria[state])

if __name__ == '__main__':
    state = 'active'
    criteria = {
        'active': lambda x: x == 'active',
        'valid': lambda x: len(x) > 0,
        'numeric': lambda x: x.isdigit()
    }
    print(validate_state(state, criteria))