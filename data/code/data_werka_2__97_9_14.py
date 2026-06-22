TRUE_VAL = True
FALSE_VAL = False
AND_OP = 'AND'
OR_OP = 'OR'
XOR_OP = 'XOR'
NOT_A_OP = 'NOT A'
NOT_B_OP = 'NOT B'
INPUT_A = 'A'
INPUT_B = 'B'
HEADER_ROW = [INPUT_A, INPUT_B, AND_OP, OR_OP, XOR_OP, NOT_A_OP, NOT_B_OP]
SEPARATOR_CHAR = '-'
SEPARATOR_WIDTH = 45
INPUTS = [TRUE_VAL, FALSE_VAL]

def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    
    table_rows = []
    
    for current_a in INPUTS:
        for current_b in INPUTS:
            and_result = current_a and current_b
            or_result = current_a or current_b
            xor_result = current_a != current_b
            not_a_result = not current_a
            not_b_result = not current_b
            
            row_data = [
                current_a,
                current_b,
                and_result,
                or_result,
                xor_result,
                not_a_result,
                not_b_result
            ]
            table_rows.append(row_data)
            
    print(SEPARATOR_CHAR * SEPARATOR_WIDTH)
    print(f"{HEADER_ROW[0]:<5} {HEADER_ROW[1]:<5} {HEADER_ROW[2]:<9} {HEADER_ROW[3]:<9} {HEADER_ROW[4]:<9} {HEADER_ROW[5]:<7} {HEADER_ROW[6]:<7}")
    print(SEPARATOR_CHAR * SEPARATOR_WIDTH)
    
    for row in table_rows:
        print(f"{str(row[0]):<5} {str(row[1]):<5} {str(row[2]):<9} {str(row[3]):<9} {str(row[4]):<9} {str(row[5]):<7} {str(row[6]):<7}")
    print(SEPARATOR_CHAR * SEPARATOR_WIDTH)
    
    return table_rows

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = generate_truth_table(sample_a, sample_b)
    print(result)