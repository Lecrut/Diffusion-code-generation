def run_length_encode(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_value = run_length_encode(sample_input)
    print(encoded_value)
    sample_input_none = None
    try:
        run_length_encode(sample_input_none)
    except TypeError as e:
        print(f"Caught expected error: {e}")