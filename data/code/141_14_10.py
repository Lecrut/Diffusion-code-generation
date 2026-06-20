def truth_table_and():
    return [[a and b for a in [False, True]] for b in [False, True]]

def truth_table_or():
    return [[a or b for a in [False, True]] for b in [False, True]]

def truth_table_not():
    return [[not a for a in [False, True]]]

if __name__ == '__main__':
    print("AND Truth Table:")
    print(truth_table_and())
    
    print("\nOR Truth Table:")
    print(truth_table_or())
    
    print("\nNOT Truth Table:")
    print(truth_table_not())