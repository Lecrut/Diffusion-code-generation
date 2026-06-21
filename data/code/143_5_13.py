def is_contradictory(entities1, entities2):
    return any(entity in entities2 for entity in entities1) and any(not entity.startswith('NOT ') and not entity[4:] in entities2 for entity in entities1)

if __name__ == '__main__':
    result1 = is_contradictory(["A", "B"], ["C"])
    print(f"Contradiction detected between ['A', 'B'] and ['C']: {result1}")
    result2 = is_contradictory(["A", "NOT A"], ["B"])
    print(f"Contradiction detected between ['A', 'NOT A'] and ['B']: {result2}")
    result3 = is_contradictory(["A", "B"], ["A", "C"])
    print(f"Contradiction detected between ['A', 'B'] and ['A', 'C']: {result3}")