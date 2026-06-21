def detect_conflicts(text1, text2):
    keywords = set(text1.split())
    negated_keywords = {f'not {k}' for k in keywords}
    return any((k in negated_keywords for k in text2.split()))
if __name__ == '__main__':
    print(detect_conflicts('hot', 'not hot'))
    print(detect_conflicts('cold', 'not cold'))
    print(detect_conflicts('big', 'small'))
    print(detect_conflicts('big', 'not small'))