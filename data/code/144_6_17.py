NAND_TABLE = {
    (False, False): True,
    (False, True): True,
    (True, False): True,
    (True, True): False
}

def nand_truth_table():
    return NAND_TABLE

if __name__ == '__main__':
    print(nand_truth_table())