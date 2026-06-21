def nand_truth_table():
    table = {
        (False, False): True,
        (False, True): True,
        (True, False): True,
        (True, True): False
    }
    return table

if __name__ == '__main__':
    print(nand_truth_table())