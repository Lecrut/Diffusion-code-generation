import sys

def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    result_parts = []
    current_char = input_string[0]
    current_count = 1
    length = len(input_string)
    for index in range(1, length):
        next_char = input_string[index]
        if next_char == current_char:
            current_count += 1
        else:
            result_parts.append(str(current_count))
            result_parts.append(current_char)
            current_char = next_char
            current_count = 1
    result_parts.append(str(current_count))
    result_parts.append(current_char)
    return "".join(result_parts)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)