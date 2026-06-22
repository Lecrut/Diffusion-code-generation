import sys

def run_length_encode(data: str) -> str:
    if not data:
        return ""

    result = []
    current_char = data[0]
    count = 1
    length = len(data)

    index = 1
    while index < length:
        char = data[index]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
        index += 1

    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "AAAABBBCCDAA"
    compressed = run_length_encode(sample_input)
    print(compressed)