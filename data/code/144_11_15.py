def truth_table():
    return [('P', 'Q', 'A -> B') for P in [False, True] for Q in [False, True]]

if __name__ == '__main__':
    table = truth_table()
    print('\n'.join(f'{row[0]} {row[1]} {not (row[0] and not row[1])}' for row in table))