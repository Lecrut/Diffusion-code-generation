def verify_false_pair(left, right):
    if left:
        return False
    if right:
        return False
    return True

if __name__ == '__main__':
    sample_x = False
    sample_y = False
    outcome = verify_false_pair(sample_x, sample_y)
    print(outcome)