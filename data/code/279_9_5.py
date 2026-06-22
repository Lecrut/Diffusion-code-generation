class DivisibleFinder:
    def find_divisibles(self):
        return [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]

if __name__ == '__main__':
    finder = DivisibleFinder()
    divisible_numbers = finder.find_divisibles()
    for number in divisible_numbers:
        print(number)