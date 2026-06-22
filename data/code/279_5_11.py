class NumberFilter:
    def print_positive_numbers(self, start, end):
        for number in range(start, end + 1):
            if number > 0:
                print(number)

if __name__ == '__main__':
    filter_instance = NumberFilter()
    filter_instance.print_positive_numbers(-5, 5)