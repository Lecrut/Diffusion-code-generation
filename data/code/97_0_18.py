AND_TABLE = {True: {True: True, False: False}, False: {True: False, False: False}}
OR_TABLE = {True: {True: True, False: True}, False: {True: False, False: False}}
NOT_TABLE = {True: False, False: True}

def generate_truth_table():
    print("P | Q | P AND Q | P OR Q | NOT P | NOT Q")
    print("---|---|---------|--------|-------|-------")
    for p in [True, False]:
        for q in [True, False]:
            and_result = AND_TABLE[p][q]
            or_result = OR_TABLE[p][q]
            not_p = NOT_TABLE[p]
            not_q = NOT_TABLE[q]
            print(f"{p} | {q} | {and_result}    | {or_result}| {not_p}   | {not_q}")

if __name__ == '__main__':
    generate_truth_table()