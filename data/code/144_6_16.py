def nand_table():
    return {
        (True, True): False,
        (True, False): True,
        (False, True): True,
        (False, False): True,
    }

if __name__ == '__main__':
    print(nand_table())