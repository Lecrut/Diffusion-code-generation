class ChecklistVerifier:
    CHECKLIST = (1, 5, 2, 8, 3)

    @staticmethod
    def contains_target(target):
        return target in ChecklistVerifier.CHECKLIST

if __name__ == '__main__':
    target1 = 8
    result1 = ChecklistVerifier.contains_target(target1)
    print(f"Does {target1} exist in checklist? {result1}")

    target2 = 'z'
    result2 = ChecklistVerifier.contains_target(target2)
    print(f"Does {target2} exist in checklist? {result2}")