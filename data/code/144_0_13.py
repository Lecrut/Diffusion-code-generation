def evaluate_expression(A, B, C):
    return (A and B) or not C

if __name__ == '__main__':
    A_sample = True
    B_sample = False
    C_sample = True
    
    print(f"A: {A_sample}, B: {B_sample}, C: {C_sample} -> Result: {evaluate_expression(A_sample, B_sample, C_sample)}")
    
    A_sample = False
    B_sample = True
    C_sample = False
    
    print(f"A: {A_sample}, B: {B_sample}, C: {C_sample} -> Result: {evaluate_expression(A_sample, B_sample, C_sample)}")