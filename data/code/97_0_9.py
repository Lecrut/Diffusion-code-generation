def print_truth_table(p1, q1, p2, q2):
    results = {
        "P | Q | P AND Q": [],
        "P | Q | P OR Q": [],
        "NOT P | NOT Q": []
    }
    
    def add_row(p, q, op_result):
        results[op_result].append(f"{p} | {q} | {op_result}")

    add_row(p1, q1, p1 and q1)
    add_row(p1, q2, p1 and q2)
    add_row(q1, p1, q1 and p1)
    add_row(q2, p2, q2 and p2)

    for label, data in results.items():
        print(label)
        print("---|---|---------")
        for row in data:
            print(row)

if __name__ == '__main__':
    print_truth_table(True, False, True, True)