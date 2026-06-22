def print_numbers():
    number_map = {i: i for i in range(10)}
    for key in sorted(number_map):
        print(key)

if __name__ == '__main__':
    print_numbers()