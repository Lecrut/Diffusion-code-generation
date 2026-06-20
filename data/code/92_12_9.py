TRUTH_VALUES = {'True': True, 'False': False}

def get_opposite(value_str):
    value = TRUTH_VALUES.get(value_str.capitalize(), None)
    if value is not None:
        return str(not value).capitalize()
    else:
        raise ValueError("Invalid truth value")

if __name__ == '__main__':
    sample1 = "True"
    opposite1 = get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    
    sample2 = "false"
    opposite2 = get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")