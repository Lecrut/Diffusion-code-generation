def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = s[i]
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "WWWWBBWW"
    result = run_length_encode(sample_string)
    print(result)
    empty_string = ""
    print(run_length_encode(empty_string))
    single_char = "Z"
    print(run_length_encode(single_char))