def is_contradictory(list1, list2):
    oppositions = {
        'A': 'NOT A',
        'B': 'NOT B',
        'C': 'NOT C'
    }
    return any(oppositions.get(item) in list2 for item in list1)

if __name__ == '__main__':
    constraints1 = ["A", "B"]
    result1 = is_contradictory(constraints1, ["NOT A"])
    print(f"Constraints: {constraints1}, Contradiction detected: {result1}")

    constraints2 = ["A", "NOT A"]
    result2 = is_contradictory(constraints2, ["B", "C"])
    print(f"Constraints: {constraints2}, Contradiction detected: {result2}")

    constraints3 = ["A", "B"]
    result3 = is_contradictory(constraints3, ["C", "NOT B"])
    print(f"Constraints: {constraints3}, Contradiction detected: {result3}")