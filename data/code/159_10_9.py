def generate_odd_numbers(limit):
    return [num for num in range(1, limit + 1) if num % 2 != 0]

if __name__ == '__main__':
    sample_limit = 50
    odd_list = generate_odd_numbers(sample_limit)
    print(odd_list)