def nand_table():
    table = {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 0
    }
    return table

if __name__ == '__main__':
    print(nand_table())