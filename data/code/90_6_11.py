OR_THRESHOLD = 10

def check_conditions(value):
    return value > OR_THRESHOLD or value == OR_THRESHOLD

if __name__ == '__main__':
    sample_value = 5
    result = check_conditions(sample_value)
    print(result)