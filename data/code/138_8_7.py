def validate_truth_table():
    for A in [True, False]:
        for B in [True, False]:
            result = (A and B) or (not A and not B)
            if not result:
                return False
    return True

if __name__ == '__main__':
    print(validate_truth_table())