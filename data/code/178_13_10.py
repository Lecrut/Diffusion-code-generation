import re

def clean_and_split(phrase):
    cleaned = re.sub(r'\W+', ' ', phrase).lower()
    return cleaned.split()

if __name__ == '__main__':
    sample_phrase = "This is a complex example phrase with various words and punctuation."
    result = clean_and_split(sample_phrase)
    print(result)