def check_evenness(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [-5, -2, -1, 0, 1, 2, 100, -100]
    for val in sample_values:
        result = check_evenness(val)
        print(f"{val}: {result}")