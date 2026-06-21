A = True
B = False
C = True

def compute_expression(a, b, c):
    return (a and b) or not c

if __name__ == '__main__':
    print(f"A: {A}, B: {B}, C: {C}")
    print(f"Result: {compute_expression(A, B, C)}")