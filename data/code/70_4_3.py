if __name__ == '__main__':
    sample_input = "60 70 80 90 100"
    numbers = list(map(int, sample_input.split()))
    if numbers:
        print(numbers[0], numbers[-1])