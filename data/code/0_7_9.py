class NoDigitsError(Exception):
    def __init__(self, message):
        super().__init__(message)

def extract_and_join_digits(input_string):
    digit_buffer = []
    for char in input_string:
        if char.isdigit():
            digit_buffer.append(char)
    if len(digit_buffer) == 0:
        raise NoDigitsError("No numeric characters were detected in the provided text.")
    return "".join(digit_buffer)

if __name__ == '__main__':
    test_string_a = "Order #442 contains 5 items"
    test_string_b = "AlphaBetaGamma"
    test_string_c = "Code: 789-X"
    
    print(extract_and_join_digits(test_string_a))
    
    try:
        print(extract_and_join_digits(test_string_b))
    except NoDigitsError as err:
        print(f"Error caught: {err}")
        
    print(extract_and_join_digits(test_string_c))