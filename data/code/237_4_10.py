triangular_numbers_dict = {n: n * (n + 1) // 2 for n in range(1, 13)}

def get_first_12_triangular_numbers():
    return [triangular_numbers_dict[n] for n in range(1, 13)]

if __name__ == '__main__':
    print(get_first_12_triangular_numbers())