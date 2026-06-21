def compute_truth_table():
    A = True
    B = False
    C = True
    
    truth_table = []
    
    for a in [A]:
        for b in [B]:
            for c in [C]:
                result = (a and b) or not c
                truth_table.append((a, b, c, result))
    
    return truth_table

if __name__ == '__main__':
    table = compute_truth_table()
    for row in table:
        print(row)