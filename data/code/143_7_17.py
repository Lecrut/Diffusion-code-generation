KEY_WORDS = set(['and', 'or', 'not', 'True', 'False'])

def evaluate_contradiction(s1: str, s2: str) -> bool:
    s1_parts = {word for word in s1.lower().split(';') if word in KEY_WORDS}
    s2_parts = {word for word in s2.lower().split(';') if word in KEY_WORDS}
    if s1_parts == {'not', 'true'} and s2_parts == {'false'}:
        return True
    if s1_parts == {'not', 'false'} and s2_parts == {'true'}:
        return True
    if not s1_parts.isdisjoint(s2_parts):
        return False
    return True
if __name__ == '__main__':
    print(evaluate_contradiction('A and B; not A', 'B'))
    print(evaluate_contradiction('True', 'False'))
    print(evaluate_contradiction('not A', 'A and not B'))