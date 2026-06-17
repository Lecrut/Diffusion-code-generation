if __name__ == '__main__':
    lower_bound = 2
    upper_bound = 10
    even_numbers = []
    for number in range(lower_bound, upper_bound + 1):
        if number % 2 == 0:
            even_numbers.append(number)
    print(*even_numbers)