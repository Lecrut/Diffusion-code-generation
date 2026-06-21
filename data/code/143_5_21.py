def is_contradictory(entities1, entities2):
    return any(e1 == "NOT " + e2 for e1 in entities1 for e2 in entities2)

if __name__ == '__main__':
    constraints1 = ["A", "B"]
    result1 = is_contradictory(constraints1, constraints1)
    print(f"Constraints: {constraints1}, Contradiction detected: {result1}")
    
    constraints2 = ["A", "NOT A"]
    result2 = is_contradictory(constraints2, constraints2)
    print(f"Constraints: {constraints2}, Contradiction detected: {result2}")
    
    constraints3 = ["B", "C", "NOT B"]
    result3 = is_contradictory(constraints3, constraints3)
    print(f"Constraints: {constraints3}, Contradiction detected: {result3}")