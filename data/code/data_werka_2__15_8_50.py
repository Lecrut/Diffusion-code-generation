def check_match(value1, value2):
    EXACT_MATCH = True
    NO_MATCH = False
    
    return EXACT_MATCH if value1 == value2 else NO_MATCH

if __name__ == '__main__':
    sample_value1 = {"key": "value"}
    sample_value2 = {"key": "value"}
    result = check_match(sample_value1, sample_value2)
    print(result)