def detect_conflicts(text1, text2):
    keywords = {'not', 'no', 'never', 'don\'t', 'cannot'}
    words1 = set(word.lower() for word in text1.split())
    negated_words2 = {word[3:] if word.startswith('do not') else word for word in text2.split()}
    conflicts = [word for word in negated_words2 if word in keywords and word in words1]
    return conflicts

if __name__ == '__main__':
    print(detect_conflicts("I can eat", "Do not eat"))