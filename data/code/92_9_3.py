def find_opposite_truth(value):
    table = {True: False, False: True}
    return table[value]

if __name__ == '__main__':
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))