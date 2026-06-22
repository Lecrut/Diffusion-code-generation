def run_length_encode(s: str) -> str:
    if not s:
        return ""

    encoded_parts = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1

    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_inputs = [
        "AAAABBBCCDAA",
        "abcd",
        "AABBCC",
        "EEEEEEEE",
        "",
        "XYZXYZ",
        "1122333",
    ]

    for sample in sample_inputs:
        result = run_length_encode(sample)
        print(f"Input: '{sample}' -> Output: '{result}'")