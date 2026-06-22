def rle_generator(data):
    if not data:
        return
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            yield count, current_char
            current_char = char
            count = 1
    yield count, current_char

def run_length_encode(data):
    return "".join(f"{count}{char}" for count, char in rle_generator(data))

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)