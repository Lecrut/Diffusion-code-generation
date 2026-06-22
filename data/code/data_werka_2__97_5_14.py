def generate_truth_table():
    headers = ['A', 'B', 'C', 'D']
    print(f"{headers[0]:<5} {headers[1]:<5} {headers[2]:<5} {headers[3]:<5} | Result")
    print("-" * 30)
    
    for i in range(16):
        A = (i >> 3) & 1
        B = (i >> 2) & 1
        C = (i >> 1) & 1
        D = (i >> 0) & 1
        
        result = A and B or (C and not D)
        
        print(f"{A:<5} {B:<5} {C:<5} {D:<5} | {result}")

if __name__ == '__main__':
    generate_truth_table()