def validate_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            result = (a and b) or (not a and not b)
            if not result:
                return False
    return True

if __name__ == '__main__':
    print(validate_truth_table())