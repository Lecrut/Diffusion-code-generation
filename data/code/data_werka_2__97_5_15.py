def generate_truth_table():
    headers = ['A', 'B', 'C', 'D']
    print(f"{headers[0]:<5} {headers[1]:<5} {headers[2]:<5} {headers[3]:<5} | Result")
    print("-" * 25)
    
    for i in range(16):
        a = (i >> 3) & 1
        b = (i >> 2) & 1
        c = (i >> 1) & 1
        d = i & 1
        
        result = (a and b) or (c and not d)
        
        print(f"{a:<5} {b:<5} {c:<5} {d:<5} | {int(result)}")

if __name__ == '__main__':
    generate_truth_table()