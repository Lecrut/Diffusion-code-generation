def run_length_encode(sequence: str) -> str:
    if not sequence:
        return ""
    
    result = []
    count = 1
    length = len(sequence)
    
    for i in range(1, length):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            result.append(f"{count}{sequence[i - 1]}")
            count = 1
    
    result.append(f"{count}{sequence[length - 1]}")
    
    return "".join(result)

if __name__ == '__main__':
    sample = "AAAABBBCCDAA"
    encoded = run_length_encode(sample)
    print(encoded)