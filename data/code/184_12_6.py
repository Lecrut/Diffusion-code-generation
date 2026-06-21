import re

class WordSearcher:
    CASE_INSENSITIVE_FLAG = re.IGNORECASE
    
    @staticmethod
    def compile_pattern(target):
        return re.compile(re.escape(target), flags=WordSearcher.CASE_INSENSITIVE_FLAG)
    
    @staticmethod
    def find_target_word(words, target):
        pattern = WordSearcher.compile_pattern(target)
        return any(pattern.search(word) for word in words)

if __name__ == '__main__':
    sample_words = ["Hello", "world", "Python", "programming"]
    target_word = "python"
    result = WordSearcher.find_target_word(sample_words, target_word)
    print(result)