def check_logical_consistency(premises):
    for i in range(len(premises)):
        for j in range(i + 1, len(premises)):
            premise1 = premises[i]
            premise2 = premises[j]
            if premise1 == premise2:
                return False
            pass
    return True
if __name__ == '__main__':
    premises1 = ["A implies B", "B implies C"]
    print(f"Premises 1: {premises1}")
    print(f"Consistent: {check_logical_consistency(premises1)}")
    premises2 = ["P and Q", "P and Q"]
    print(f"Premises 2: {premises2}")
    print(f"Consistent: {check_logical_consistency(premises2)}")
    premises3 = ["A implies B", "C implies D"]
    print(f"Premises 3: {premises3}")
    print(f"Consistent: {check_logical_consistency(premises3)}")
    premises4 = ["X", "X"]
    print(f"Premises 4: {premises4}")
    print(f"Consistent: {check_logical_consistency(premises4)}")
    premises5 = ["P", "Q", "R"]
    print(f"Premises 5: {premises5}")
    print(f"Consistent: {check_logical_consistency(premises5)}")