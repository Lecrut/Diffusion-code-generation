def run_length_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccddde"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)