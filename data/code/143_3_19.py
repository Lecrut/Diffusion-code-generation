def detect_conflicts(text1, text2):
    keywords = set(text1.split())
    negated_keywords = {f'not {keyword}' for keyword in keywords}
    if any((keyword in text2 for keyword in negated_keywords)):
        return True
    return False
if __name__ == '__main__':
    print(detect_conflicts('apple orange', 'I have an apple'))
    print(detect_conflicts('apple orange', 'I do not have an apple'))
    print(detect_conflicts('red blue', 'The sky is red'))
    print(detect_conflicts('red blue', 'The sky is not red'))