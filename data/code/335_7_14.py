import re
def split_sentence(sentence: str) -> list[str]:
    words = sentence.strip().split()
    return [word for word in words if len(word) > 1]
if __name__ == '__main__':
    sample_input = "Hello world, this is a test."
    result = split_sentence(sample_input)
    print(result)