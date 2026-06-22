import sys

def run_length_encode(input_string):
    if not input_string:
        return ""
    result = []
    count = 1
    length = len(input_string)
    current_char = input_string[0]
    for i in range(1, length):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = input_string[i]
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    encoded_output = run_length_encode(sample_data)
    print(encoded_output)