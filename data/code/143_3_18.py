def detect_conflicts(text1, text2):
    keywords = set(text1.split())
    negated_keywords = {f"not {keyword}" for keyword in keywords}
    return any(keyword in text2 or negated_keyword in text2 for keyword in keywords for negated_keyword in negated_keywords)

if __name__ == '__main__':
    print(detect_conflicts("hot weather", "it is not hot"))