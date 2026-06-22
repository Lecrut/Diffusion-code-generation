import sys

def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = data[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdddd"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    
    single_char_input = "z"
    single_result = run_length_encode(single_char_input)
    print(single_result)