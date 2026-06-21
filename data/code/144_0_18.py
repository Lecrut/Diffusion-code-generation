def compute_expression(A, B, C):
    return (A and B) or not C

if __name__ == '__main__':
    sample_values = {
        'A': True,
        'B': False,
        'C': True
    }
    
    for A, B, C in [(True, True, True), (True, False, True), (False, True, True), (False, False, True)]:
        print(f"A: {A}, B: {B}, C: {C}, Result: {compute_expression(A, B, C)}")