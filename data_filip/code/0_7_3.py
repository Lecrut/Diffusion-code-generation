class NoDigitsFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

DIGIT_RANGE_START = 0
DIGIT_RANGE_END = 10

def is_numeric_char(character):
    return DIGIT_RANGE_START <= ord(character) <= DIGIT_RANGE_END or character.isdecimal()

def collect_digits(text):
    collected = []
    for char in text:
        if char.isdigit():
            collected.append(char)
    return collected

def extract_and_join_digits(mixed_text):
    digits = collect_digits(mixed_text)
    if len(digits) == 0:
        raise NoDigitsFoundError("The input string contains no numeric characters.")
    return "".join(digits)

if __name__ == '__main__':
    input_a = "Order#9924-Alpha"
    input_b = "PureTextString"
    input_c = "404 Error"
    
    try:
        print(extract_and_join_digits(input_a))
    except NoDigitsFoundError as err:
        print(err)
        
    try:
        print(extract_and_join_digits(input_b))
    except NoDigitsFoundError as err:
        print(err)
        
    try:
        print(extract_and_join_digits(input_c))
    except NoDigitsFoundError as err:
        print(err)