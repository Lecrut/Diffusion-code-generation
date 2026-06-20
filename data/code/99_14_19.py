def validate_state(state, criteria):
    return all(criteria[state])

if __name__ == '__main__':
    sample_state = 'active'
    sample_criteria = {
        'active': lambda x: x == 'active',
        'valid': lambda x: len(x) > 0,
        'numeric': lambda x: x.isdigit()
    }
    print(validate_state(sample_state, sample_criteria))