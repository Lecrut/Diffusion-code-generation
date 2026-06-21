def run_length_encode(data):
    if data is None:
        raise TypeError("Input cannot be None")
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    if not data:
        return ""
    
    groups = []
    current_symbol = data[0]
    run_length = 1
    
    for index in range(1, len(data)):
        if data[index] == current_symbol:
            run_length += 1
        else:
            groups.append(format_group(run_length, current_symbol))
            current_symbol = data[index]
            run_length = 1
    
    groups.append(format_group(run_length, current_symbol))
    return "".join(groups)

def format_group(length, symbol):
    if length == 1:
        return symbol
    return str(length) + symbol

if __name__ == '__main__':
    test_cases = [
        "AABBBCCCC",
        "XYZ",
        "",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBB",
        "1122333"
    ]
    
    for value in test_cases:
        result = run_length_encode(value)
        print(result)