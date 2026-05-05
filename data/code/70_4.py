if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    numbers = list(map(int, sample_input.split()))
    if numbers:
        print(numbers[0], numbers[-1])