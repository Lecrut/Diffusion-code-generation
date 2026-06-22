def decompress_run_length(s):
    if not s:
        return ""
    result = []
    count = 0
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count > 0:
                result.append(char * count)
                count = 0
            else:
                result.append(char)
    if count > 0:
        result.append(result[-1] * count)
    return "".join(result)

if __name__ == '__main__':
    print(decompress_run_length("2a3b4c1d"))