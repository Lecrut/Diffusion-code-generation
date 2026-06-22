REPEAT_COUNT = 10

def repeat_characters(s: str, p: int) -> str:
    return s * p

if __name__ == '__main__':
    sample_string = "abc"
    print("Repeating 'abc' 3 times:", repeat_characters(sample_string, REPEAT_COUNT))