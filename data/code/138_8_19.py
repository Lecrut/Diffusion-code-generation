def validate_truth_table():
    values = [0, 1]
    for p in values:
        for q in values:
            if not ((p and q) or (not p and not q)):
                return False
    return True

if __name__ == '__main__':
    print(validate_truth_table())