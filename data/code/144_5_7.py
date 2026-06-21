def generate_truth_table():
    P = 0b111
    Q = 0b110
    R = 0b101
    
    for i in range(8):
        p_val = (P >> i) & 1
        q_val = (Q >> i) & 1
        r_val = (R >> i) & 1
        
        print(f"P={p_val}, Q={q_val}, R={r_val}")

if __name__ == '__main__':
    generate_truth_table()