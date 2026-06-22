MAX_REPETITIONS = 1000
PATTERN = 'AB'

def generate_pattern(n):
    return PATTERN * n

if __name__ == '__main__':
    result = generate_pattern(MAX_REPETITIONS)
    print(result)