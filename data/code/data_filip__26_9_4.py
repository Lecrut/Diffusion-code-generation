def run_length_encode():
    text = "AAAABBBCCDAA"
    result = []
    i = 0
    n = len(text)
    while i < n:
        char = text[i]
        count = 1
        while i + count < n and text[i + count] == char:
            count += 1
        result.append(str(count) + char)
        i += count
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode())