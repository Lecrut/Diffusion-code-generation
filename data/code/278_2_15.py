def print_integers(integer_list):
    index = 0
    while index < len(integer_list):
        print(integer_list[index])
        index += 1

if __name__ == '__main__':
    sample_values = [2, 4, 6, 8, 10]
    print_integers(sample_values)