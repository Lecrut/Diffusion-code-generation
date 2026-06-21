def validate_input(sentence, delimiter):
    if not isinstance(sentence, str) or not isinstance(delimiter, str):
        raise ValueError("Both sentence and delimiter must be strings.")
    if len(delimiter) == 0:
        raise ValueError("Delimiter cannot be an empty string.")

def tokenize_sentence(sentence, delimiter):
    validate_input(sentence, delimiter)
    return sentence.split(delimiter)

if __name__ == '__main__':
    sample_sentence = "Hello,world,this,is,a,test."
    delimiter = ","
    result = tokenize_sentence(sample_sentence, delimiter)
    print(result)