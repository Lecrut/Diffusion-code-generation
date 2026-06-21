def analyze_semantic_exclusivity(statement1: str, statement2: str) -> bool:
    SEMANTIC_MAP = {'dog': {'cat', 'fish'}, 'cat': {'dog', 'bird'}, 'bird': {'cat', 'fish'}, 'fish': {'dog', 'bird'}}
    set1 = set(statement1.split())
    set2 = set(statement2.split())
    for entity in set1.intersection(set2):
        if SEMANTIC_MAP.get(entity) and (not SEMANTIC_MAP[entity].isdisjoint(set1.union(set2))):
            return False
    return True
if __name__ == '__main__':
    statement1 = 'I have a dog'
    statement2 = 'I have a cat'
    print(analyze_semantic_exclusivity(statement1, statement2))