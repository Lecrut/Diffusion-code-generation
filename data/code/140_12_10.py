def validate_input(value):
    if isinstance(value, str) and value:
        return bool(re.match('^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    return False

if __name__ == '__main__':
    sample_values = ['Hello123', 42, '', 'Hello!', -5]
    for val in sample_values:
        print(f"Input: {val}, Valid: {validate_input(val)}")