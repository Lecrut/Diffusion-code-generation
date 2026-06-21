MIN_THRESHOLD = 0
MAX_THRESHOLD = 100

def validate_number(num: int) -> bool:
    return num > MIN_THRESHOLD and num < MAX_THRESHOLD and num % 2 == 0

if __name__ == '__main__':
    test_input = 42
    result = validate_number(test_input)
    print(result)