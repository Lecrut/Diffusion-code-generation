def generate_odd_numbers():
    odd_numbers = list(range(1, 101, 2))
    return odd_numbers

if __name__ == '__main__':
    sample_list = [i for i in range(1, 101) if i % 2 != 0]
    result = generate_odd_numbers()
    print(result)