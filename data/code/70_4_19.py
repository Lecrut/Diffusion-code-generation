if __name__ == '__main__':
    sample_input = "25 35 45 55 65"
    numbers = list(map(int, sample_input.split()))
    if numbers:
        print(numbers[0], numbers[-1])