def nand_truth_table():
    truth_table = {
        (False, False): True,
        (False, True): True,
        (True, False): True,
        (True, True): False
    }
    return truth_table

if __name__ == '__main__':
    print(nand_truth_table())