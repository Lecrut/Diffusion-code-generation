CHARS_PER_BATCH = 5

def char_generator(input_string):
    start = 0
    while start < len(input_string):
        end = min(start + CHARS_PER_BATCH, len(input_string))
        yield input_string[start:end]
        start = end

if __name__ == '__main__':
    test_string = "Hello World"
    generator = char_generator(test_string)
    for batch in generator:
        print(batch)