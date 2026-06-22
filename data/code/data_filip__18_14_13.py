def run_length_encode(s):
    if not s:
        return
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = s[i]
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    result = list(run_length_encode("aaabbc"))
    print(result)