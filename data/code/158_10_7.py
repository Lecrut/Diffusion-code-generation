if __name__ == '__main__':
    start = 0
    end = 50

    def is_even(number):
        return number % 2 == 0

    even_numbers = [num for num in range(start, end + 1) if is_even(num)]
    print(even_numbers)