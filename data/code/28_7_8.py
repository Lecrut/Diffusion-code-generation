def rle_encode(text):
    if not text:
        return ""
    
    def generate_runs(s):
        if not s:
            return
        iterator = iter(s)
        current_char = next(iterator)
        count = 1
        for char in iterator:
            if char == current_char:
                count += 1
            else:
                yield (current_char, count)
                current_char = char
                count = 1
        yield (current_char, count)
    
    result = []
    for char, count in generate_runs(text):
        if count == 1:
            result.append(char)
        else:
            result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "wwwwaaadexxxxxx"
    encoded = rle_encode(sample_string)
    print(encoded)