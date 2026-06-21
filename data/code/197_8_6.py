VALID_MEMBERS = (1, 5, 2, 8, 3)

def is_member(checklist):
    return any(item in checklist for item in VALID_MEMBERS)

if __name__ == '__main__':
    sample_checklist1 = (1, 9, 2)
    result1 = is_member(sample_checklist1)
    print(f"Checklist {sample_checklist1} contains valid members: {result1}")

    sample_checklist2 = (4, 5, 6)
    result2 = is_member(sample_checklist2)
    print(f"Checklist {sample_checklist2} contains valid members: {result2}")