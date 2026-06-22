def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_input = "apple banana cherry"
    try:
        words = sample_input.split()
        min_word = find_minimum(words)
        print(min_word)
    except ValueError as e:
        print(e)