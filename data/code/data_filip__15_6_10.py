def compress_sequence(seq):
    if not seq:
        return ""
    result = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            result.append(f"{seq[i - 1]}{count}")
            count = 1
    result.append(f"{seq[-1]}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample = "zzzzzxyyy"
    print(compress_sequence(sample))