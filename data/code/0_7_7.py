class EmptyDigitResult(Exception):
    def __init__(self):
        super().__init__("No digits were found in the provided string")

def isolate_numeric_characters(text):
    cleaned = []
    for item in text:
        if item.isdigit():
            cleaned.append(item)
    return cleaned

def process_mixed_input(source):
    numeric_chars = isolate_numeric_characters(source)
    if not numeric_chars:
        raise EmptyDigitResult()
    return "".join(numeric_chars)

if __name__ == '__main__':
    test_a = "a1b2c3"
    test_b = "nodigits"
    test_c = "42islife"
    
    try:
        output_a = process_mixed_input(test_a)
        print(output_a)
    except EmptyDigitResult as error:
        print(error)
        
    try:
        output_b = process_mixed_input(test_b)
        print(output_b)
    except EmptyDigitResult as error:
        print(error)
        
    try:
        output_c = process_mixed_input(test_c)
        print(output_c)
    except EmptyDigitResult as error:
        print(error)