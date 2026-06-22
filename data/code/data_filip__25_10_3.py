def run_length_encode(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{s[i - 1]}")
            count = 1
    compressed.append(f"{count}{s[-1]}")
    return "".join(compressed)

if __name__ == "__main__":
    sample_input = "aaabbcccc"
    result = run_length_encode(sample_input)
    print(result)
    empty_input = ""
    print(run_length_encode(empty_input))
    single_char = "z"
    print(run_length_encode(single_char))
    mixed = "a111bbb22c"
    print(run_length_encode(mixed))