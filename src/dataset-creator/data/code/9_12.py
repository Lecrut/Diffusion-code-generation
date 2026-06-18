if __name__ == '__main__':
    input_string = "10 20 30 40 50"
    numbers = list(map(int, input_string.split()))
    average = sum(numbers) / len(numbers)
    print(average)