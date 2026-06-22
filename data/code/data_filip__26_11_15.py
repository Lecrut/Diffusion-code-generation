def run_length_encode(s):
    if not s:
        return ''
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
    return ''.join(result)

if __name__ == '__main__':
    s = 'AAAABBBCCDAA'
    print(run_length_encode(s))