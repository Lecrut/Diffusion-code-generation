def check_parity(number):
    return (number, number % 2 == 0)

if __name__ == '__main__':
    sample_values = [10, 15, 20, 25]
    results = [check_parity(value) for value in sample_values]
    print(results)