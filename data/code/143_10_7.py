def check_contradiction(code_block):
    statements = code_block.split('if ')
    contradictory = False
    for i in range(len(statements) - 1):
        stmt1 = statements[i].strip()
        stmt2 = statements[i+1].strip()
        if 'and' in stmt1.lower() or 'or' in stmt1.lower():
            continue
        if 'not' in stmt1.lower():
            if stmt2.lower().startswith('not '):
                continue
        if stmt2.lower().startswith('not ' + stmt1.lower().replace('if ', '')):
            contradictory = True
            break
    return contradictory
if __name__ == '__main__':
    sample_code_1 = "if x > 5: print('A')"
    sample_code_2 = "if x <= 0: print('B')"
    sample_code_3 = "if x > 5: print('C')"
    sample_code_4 = "if not (x > 5): print('D')"
    sample_code_5 = "if x > 5: print('E')"
    sample_code_6 = "if not (x > 5): print('F')"
    sample_code_7 = "if x > 5: print('G')"
    sample_code_8 = "if not (x > 5): print('H')"
    print(f"Sample 1 vs 2: {check_contradiction(sample_code_1 + ' if ' + sample_code_2)}")
    print(f"Sample 3 vs 4: {check_contradiction(sample_code_3 + ' if ' + sample_code_4)}")
    print(f"Sample 5 vs 6: {check_contradiction(sample_code_5 + ' if ' + sample_code_6)}")
    print(f"Sample 7 vs 8: {check_contradiction(sample_code_7 + ' if ' + sample_code_8)}")
    print(f"Sample 1 vs 3: {check_contradiction(sample_code_1 + ' if ' + sample_code_3)}")
    print(f"Sample 2 vs 4: {check_contradiction(sample_code_2 + ' if ' + sample_code_4)}")