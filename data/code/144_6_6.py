def nand_truth_table():
    return {
        (False, False): True,
        (False, True): True,
        (True, False): True,
        (True, True): False
    }

if __name__ == '__main__':
    print(nand_truth_table())