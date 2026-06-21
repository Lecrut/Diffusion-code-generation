def nand_table():
    return {
        (False, False): True,
        (False, True): True,
        (True, False): True,
        (True, True): False
    }

if __name__ == '__main__':
    print(nand_table())