CHARACTER_COUNT = {}

def count_characters(input_string):
    for char in input_string:
        if char in CHARACTER_COUNT:
            CHARACTER_COUNT[char] += 1
        else:
            CHARACTER_COUNT[char] = 1

if __name__ == '__main__':
    sample_string = "hello world!"
    count_characters(sample_string)
    print(CHARACTER_COUNT)