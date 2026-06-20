def validate_state(state, criteria):
    return all(criteria[state])

if __name__ == '__main__':
    state = 'active'
    criteria = {
        'active': lambda x: [x == 'active'],
        'inactive': lambda x: [x != 'active']
    }
    print(validate_state(state, criteria))