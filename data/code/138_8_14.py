def check_truth_table():
    A_values = [0, 1]
    B_values = [0, 1]
    
    for a in A_values:
        for b in B_values:
            left_side = (a and b) or (not a and not b)
            right_side = True
            if left_side != right_side:
                return False
    return True

if __name__ == '__main__':
    result = check_truth_table()
    print(result)