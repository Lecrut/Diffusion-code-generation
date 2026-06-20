def validate_state(state, criteria):
    return all(criteria[state])

if __name__ == '__main__':
    sample_state = 'active'
    sample_criteria = {
        'active': lambda x: True,
        'inactive': lambda x: False,
        'pending': lambda x: x != 'active' and x != 'inactive'
    }
    print(validate_state(sample_state, sample_criteria))