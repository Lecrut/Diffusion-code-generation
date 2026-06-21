import re

class SentenceSplitter:
    DELIMITERS = r'[ ,.;!?]+'
    
    @staticmethod
    def split_sentence(sentence):
        return re.split(SentenceSplitter.DELIMITERS, sentence)
    
    @staticmethod
    def print_split_result(sentence):
        words = SentenceSplitter.split_sentence(sentence)
        print(f"Original Text: '{sentence}'")
        print("Split Words:")
        for word in words:
            if word:
                print(word)

if __name__ == '__main__':
    sample_text = "This is a sample sentence. It contains various delimiters like commas, periods, and exclamation marks! We will split this text to demonstrate the SentenceSplitter class."
    SentenceSplitter.print_split_result(sample_text)