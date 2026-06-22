class ExtractionError(Exception):
    def __init__(self, message):
        super().__init__(message)

DIGIT_CHARS = "0123456789"

def isolate_numeric_sequence(text):
    buffer = []
    for symbol in text:
        if symbol in DIGIT_CHARS:
            buffer.append(symbol)
    return buffer

def construct_digit_string(source_text):
    collected_sequence = isolate_numeric_sequence(source_text)
    if len(collected_sequence) == 0:
        raise ExtractionError("The provided text lacks any numeric digits.")
    return "".join(collected_sequence)

if __name__ == '__main__':
    scenario_one = "Room 304-B"
    scenario_two = "alpha-beta-gamma"
    scenario_three = "ID: 998877"
    
    try:
        print(construct_digit_string(scenario_one))
    except ExtractionError as error:
        print(error)
    
    try:
        print(construct_digit_string(scenario_two))
    except ExtractionError as error:
        print(error)
        
    try:
        print(construct_digit_string(scenario_three))
    except ExtractionError as error:
        print(error)