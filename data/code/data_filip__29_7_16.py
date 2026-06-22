def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    count = 1
    char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == char:
            count += 1
        else:
            result.append(f"{count}{char}")
            char = input_string[i]
            count = 1
    result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    test_string = "AAAABBBCCDAA"
    encoded_result = run_length_encode(test_string)
    print(encoded_result)