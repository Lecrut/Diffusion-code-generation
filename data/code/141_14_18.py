def truth_table_and():
    return [[a and b for b in [False, True]] for a in [False, True]]

def truth_table_or():
    return [[a or b for b in [False, True]] for a in [False, True]]

def truth_table_not():
    return [[not a] for a in [False, True]]

if __name__ == '__main__':
    and_table = truth_table_and()
    or_table = truth_table_or()
    not_table = truth_table_not()

    print("AND Truth Table:")
    for row in and_table:
        print(row)

    print("\nOR Truth Table:")
    for row in or_table:
        print(row)

    print("\nNOT Truth Table:")
    for row in not_table:
        print(row)