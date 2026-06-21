def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(data[i - 1])
            result.append(str(count))
            count = 1
    
    result.append(data[-1])
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    test_strings = ["aaabbc", "abcdef", "aaaa", ""]
    for s in test_strings:
        encoded = run_length_encode(s)
        print(encoded)