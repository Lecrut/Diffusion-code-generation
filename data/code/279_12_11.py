def print_even_numbers():
    for num in range(100):
        if num % 2 == 0:
            print(num)

if __name__ == '__main__':
    sample_values = [0, 5, 98]
    for value in sample_values:
        print(f"Even numbers up to {value}:")
        print_even_numbers()