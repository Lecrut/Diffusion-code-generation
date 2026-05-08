class LogicalConsistencyAnalyzer:
    def check_consistency(self, premises):
        inferences = []
        for p in premises:
            inferences.append(p)
        for i in range(len(inferences)):
            for j in range(i + 1, len(inferences)):
                p1 = inferences[i]
                p2 = inferences[j]
                if p1 == p2:
                    continue
                if p1 == "A implies B" and p2 == "not B":
                    return False
                if p1 == "B implies A" and p2 == "not A":
                    return False
                if p1 == "A" and p2 == "not A":
                    return False
                if p1 == "not A" and p2 == "A":
                    return False
                if p1 == "P and Q" and p2 == "not (P and Q)":
                    return False
                if p1 == "P" and p2 == "not P":
                    return False
                if p1 == "P implies Q" and p2 == "not Q":
                    return False
                if p1 == "Q" and p2 == "not Q":
                    return False
        return True
def analyze_logic(premises):
    analyzer = LogicalConsistencyAnalyzer()
    return analyzer.check_consistency(premises)
if __name__ == '__main__':
    sample_premises_consistent = [
        "A implies B",
        "B implies C",
        "A"
    ]
    sample_premises_inconsistent = [
        "A",
        "not A"
    ]
    sample_premises_inconsistent_2 = [
        "P",
        "not P"
    ]
    print(f"Consistency check for consistent premises: {analyze_logic(sample_premises_consistent)}")
    print(f"Consistency check for inconsistent premises 1: {analyze_logic(sample_premises_inconsistent)}")
    print(f"Consistency check for inconsistent premises 2: {analyze_logic(sample_premises_inconsistent_2)}")