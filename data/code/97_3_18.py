P_TRUE = 1
P_FALSE = 0

def generate_truth_table():
    header = "P | Q | (P -> Q)"
    print(header)
    print("-" * len(header))
    
    for p in [P_TRUE, P_FALSE]:
        for q in [P_TRUE, P_FALSE]:
            result = (not p) or q
            print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    generate_truth_table()