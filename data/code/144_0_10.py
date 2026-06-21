def compute_truth_table():
    A = True
    B = False
    C = True
    
    result = (A and B) or not C
    print(f"({A} AND {B}) OR NOT {C}: {result}")

if __name__ == '__main__':
    compute_truth_table()