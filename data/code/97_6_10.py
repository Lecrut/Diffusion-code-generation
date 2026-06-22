TRUE_VAL = True
FALSE_VAL = False
COL_WIDTH = 6
SEPARATOR_CHAR = "-"
HEADER_SEP_LEN = 70

def generate_truth_table(inputs):
    headers = ["P", "Q", "P AND Q", "P OR Q", "P XOR Q", "NOT P", "P IMPLIES Q"]
    print(SEPARATOR_CHAR * HEADER_SEP_LEN)
    print(f"{headers[0]:<{COL_WIDTH}} {headers[1]:<{COL_WIDTH}} {headers[2]:<{COL_WIDTH}} {headers[3]:<{COL_WIDTH}} {headers[4]:<{COL_WIDTH}} {headers[5]:<{COL_WIDTH}} {headers[6]:<{COL_WIDTH}}")
    print(SEPARATOR_CHAR * HEADER_SEP_LEN)
    for p, q in inputs:
        col_and = p and q
        col_or = p or q
        col_xor = p != q
        col_not = not p
        col_implies = (not p) or q
        print(f"{str(p):<{COL_WIDTH}} {str(q):<{COL_WIDTH}} {str(col_and):<{COL_WIDTH}} {str(col_or):<{COL_WIDTH}} {str(col_xor):<{COL_WIDTH}} {str(col_not):<{COL_WIDTH}} {str(col_implies):<{COL_WIDTH}}")

if __name__ == '__main__':
    sample_inputs = [
        (TRUE_VAL, TRUE_VAL),
        (TRUE_VAL, FALSE_VAL),
        (FALSE_VAL, TRUE_VAL),
        (FALSE_VAL, FALSE_VAL)
    ]
    generate_truth_table(sample_inputs)