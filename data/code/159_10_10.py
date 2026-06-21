def find_odd_numbers(limit=50):
    return [num for num in range(1, limit + 1) if num % 2 != 0]

if __name__ == '__main__':
    odd_numbers = find_odd_numbers()
    print(odd_numbers)