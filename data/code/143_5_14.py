def is_contradictory(list1, list2):
    def is_opposite(a, b):
        return (a == 'NOT ' + b) or (b == 'NOT ' + a)
    
    for item in list1:
        if any(is_opposite(item, other) for other in list2):
            return True
    return False

if __name__ == '__main__':
    constraints1 = ["A", "B"]
    result1 = is_contradictory(constraints1, constraints1)
    print(f"Constraints: {constraints1}, Contradiction detected: {result1}")
    
    constraints2 = ["A", "NOT A"]
    result2 = is_contradictory(constraints2, constraints2)
    print(f"Constraints: {constraints2}, Contradiction detected: {result2}")
    
    constraints3 = ["A", "B"]
    result3 = is_contradictory(constraints1, constraints3)
    print(f"Constraints: {constraints1}, {constraints3}, Contradiction detected: {result3}")