AND_TABLE = {
    (True, True): True,
    (True, False): False,
    (False, True): False,
    (False, False): False
}

def generate_and_truth_table():
    for combo in AND_TABLE:
        print(f"{combo[0]} AND {combo[1]} = {AND_TABLE[combo]}")

if __name__ == '__main__':
    generate_and_truth_table()