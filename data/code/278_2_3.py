def print_integers(integer_list):
    index = 0
    while index < len(integer_list):
        print(integer_list[index])
        index += 1

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print_integers(sample_values)