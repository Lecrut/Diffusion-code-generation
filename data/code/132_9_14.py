def determine_outcome():
    A = True
    B = False
    C = True
    result = A & B | ~C
    return result
if __name__ == '__main__':
    outcome = determine_outcome()
    print(outcome)