TEXT_TO_SPLIT = "this is a test string"

def split_and_reverse(text):
    parts = text.split()
    reversed_parts = parts[::-1]
    return reversed_parts

if __name__ == '__main__':
    result = split_and_reverse(TEXT_TO_SPLIT)
    print(result)