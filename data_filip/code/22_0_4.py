def compress_string(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    length = len(data)
    for index in range(1, length):
        if data[index] == data[index - 1]:
            count += 1
        else:
            result.append(data[index - 1])
            result.append(str(count))
            count = 1
    result.append(data[length - 1])
    result.append(str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbbcccaaa"
    print(compress_string(sample_input))
    print(compress_string(""))
    print(compress_string("x"))
    print(compress_string("xxxyyyyyzz"))