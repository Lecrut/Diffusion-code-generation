def validate_input(sentence: str, delimiter: str):
    if not isinstance(sentence, str) or not isinstance(delimiter, str):
        raise ValueError("Both sentence and delimiter must be strings.")
    if len(delimiter) != 1:
        raise ValueError("Delimiter must be a single character.")

def tokenize_sentence(sentence: str, delimiter: str) -> list:
    validate_input(sentence, delimiter)
    return sentence.split(delimiter)

if __name__ == '__main__':
    sample_sentence = "Hello,world,this,is,a,test."
    delimiter = ","
    words = tokenize_sentence(sample_sentence, delimiter)
    print(words)