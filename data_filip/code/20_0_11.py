def run_length_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    count = 1
    previous = text[0]
    for index in range(1, len(text)):
        current = text[index]
        if current == previous:
            count += 1
        else:
            result.append(f"{previous}{count}")
            previous = current
            count = 1
    result.append(f"{previous}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)