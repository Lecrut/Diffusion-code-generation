def check_logical_consistency(premises):
    for i in range(len(premises)):
        for j in range(i + 1, len(premises)):
            premise1 = premises[i]
            premise2 = premises[j]
            if premise1 == premise2:
                return False
            if premise1 == f"P and not P":
                return False
            if premise2 == f"Q and not Q":
                return False
            if premise1 == "A" and premise2 == "not A":
                return False
            if premise1 == "B" and premise2 == "not B":
                return False
            if premise1 == "P" and premise2 == "not P":
                return False
            if premise1 == "Q" and premise2 == "not Q":
                return False
            if premise1 == "R" and premise2 == "not R":
                return False
            if premise1 == "S" and premise2 == "not S":
                return False
            if premise1 == "T" and premise2 == "not T":
                return False
    return True
if __name__ == '__main__':
    sample1 = ["P", "Q"]
    sample2 = ["P", "P"]
    sample3 = ["P", "not P"]
    sample4 = ["A", "not A"]
    sample5 = ["P", "Q", "R"]
    sample6 = ["P", "P and not P"]
    sample7 = ["A", "not A", "B"]
    print(f"Sample 1 {sample1}: {check_logical_consistency(sample1)}")
    print(f"Sample 2 {sample2}: {check_logical_consistency(sample2)}")
    print(f"Sample 3 {sample3}: {check_logical_consistency(sample3)}")
    print(f"Sample 4 {sample4}: {check_logical_consistency(sample4)}")
    print(f"Sample 5 {sample5}: {check_logical_consistency(sample5)}")
    print(f"Sample 6 {sample6}: {check_logical_consistency(sample6)}")
    print(f"Sample 7 {sample7}: {check_logical_consistency(sample7)}")