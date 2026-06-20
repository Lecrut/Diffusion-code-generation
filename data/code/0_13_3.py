def extract_floats(text):
    numbers = []
    current_number = []
    in_number = False
    has_decimal = False
    
    for char in text:
        if char.isdigit() or char == '.':
            if char == '.':
                if has_decimal:
                    if current_number:
                        number_str = ''.join(current_number)
                        if number_str:
                            numbers.append(float(number_str))
                            current_number = []
                            has_decimal = False
                    else:
                        has_decimal = False
                        current_number = []
                    continue
                else:
                    has_decimal = True
            current_number.append(char)
            in_number = True
        else:
            if current_number:
                number_str = ''.join(current_number)
                if number_str:
                    numbers.append(float(number_str))
                    current_number = []
                    has_decimal = False
                else:
                    current_number = []
                    has_decimal = False
            in_number = False
    
    if current_number:
        number_str = ''.join(current_number)
        if number_str:
            numbers.append(float(number_str))
    
    return numbers

if __name__ == '__main__':
    sample_text = "There are 3.14 apples, 42 oranges, and 0.005 bananas. Also -7.5 and 100."
    result = extract_floats(sample_text)
    print(result)