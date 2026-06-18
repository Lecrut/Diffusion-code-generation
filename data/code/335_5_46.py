from typing import List
def split_sentence(sentence: str) -> List[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello world this is a test"
    result = split_sentence(sample_input)
    print(result)