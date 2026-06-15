import time
def separate_characters(input_string):
    characters = []
    for char in input_string:
        if isinstance(char, str) and len(char) == 1:
            characters.append(char)
    return "".join(characters)
if __name__ == '__main__':
    sample_string = "Hello World!123"
    start_time = time.perf_counter()
    result = separate_characters(sample_string)
    end_time = time.perf_counter()
    print(result)