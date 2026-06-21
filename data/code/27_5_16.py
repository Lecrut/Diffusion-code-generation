def rle_encode(s):
    if not s:
        return ""
    result = []
    chars = zip(s, s[1:] + ' ')
    count = 1
    prev_char = s[0]
    for curr_char, _ in chars:
        if curr_char != prev_char:
            result.append(f"{prev_char}{count}")
            count = 0
            prev_char = curr_char
        count += 1
    result.append(f"{prev_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    print(rle_encode("AAAAABBBB"))