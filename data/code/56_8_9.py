MULTIPLIER_START = 1
MULTIPLIER_END = 11
TARGET_NUMBER = 6

def validate_input(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number <= 0:
        raise ValueError("Input must be a positive integer")

def build_table(number):
    validate_input(number)
    result = {}
    current = MULTIPLIER_START
    while current < MULTIPLIER_END:
        result[current] = number * current
        current += 1
    return result

if __name__ == '__main__':
    sample_number = 6
    table_data = build_table(sample_number)
    print(table_data)