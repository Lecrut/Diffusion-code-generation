class DivisibleNumbers:
    def print_divisibles(self):
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                print(number)

if __name__ == '__main__':
    divisible_numbers = DivisibleNumbers()
    divisible_numbers.print_divisibles()