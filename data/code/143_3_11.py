def detect_conflicts(text1, text2):
    keywords = {'not', 'no', 'never', 'don\'t', 'cannot'}
    words2 = set(text2.lower().split())
    negated_keywords = {f'not {k}' for k in keywords} | {f'{k} not' for k in keywords}
    conflicts = [word for word in negated_keywords if word in words2]
    return conflicts

if __name__ == '__main__':
    print(detect_conflicts("I can do it", "I cannot do it"))