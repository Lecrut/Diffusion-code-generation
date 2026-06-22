def print_integers(integer_list):
    INDEX = 0
    while INDEX < len(integer_list):
        print(integer_list[INDEX])
        INDEX += 1

if __name__ == '__main__':
    SAMPLE_VALUES = [1, 2, 3, 4, 5]
    print_integers(SAMPLE_VALUES)