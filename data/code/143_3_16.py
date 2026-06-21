KEYWORDS = {'and', 'or', 'not'}

def detect_conflicts(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    for keyword in KEYWORDS:
        if keyword in words1 and keyword not in words2:
            return True
        elif keyword not in words1 and keyword in words2:
            return True
    return False
if __name__ == '__main__':
    print(detect_conflicts('I love dogs', 'I hate cats'))
    print(detect_conflicts('I love dogs', 'I love cats'))
    print(detect_conflicts('I love dogs and I hate cats', 'I love dogs'))
    print(detect_conflicts('I love dogs', 'I love dogs and I hate cats'))