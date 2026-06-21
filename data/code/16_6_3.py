def run_length_encode(strings: list[str]) -> list[str]:
    if not strings:
        return []

    result = []
    count = 1
    current = strings[0]

    for i in range(1, len(strings)):
        if strings[i] == current:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}:{current}")
            else:
                result.append(current)
            current = strings[i]
            count = 1

    if count > 1:
        result.append(f"{count}:{current}")
    else:
        result.append(current)

    return result

if __name__ == '__main__':
    sample_data = ["a", "a", "b", "b", "b", "c", "a", "a", "a", "a"]
    encoded = run_length_encode(sample_data)
    print(encoded)