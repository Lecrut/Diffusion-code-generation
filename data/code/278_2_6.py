MAX_ITERATIONS = 10

def print_integers(integer_list):
    index = 0
    while index < len(integer_list) and index < MAX_ITERATIONS:
        print(integer_list[index])
        index += 1

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print_integers(sample_values)