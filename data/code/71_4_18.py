class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_middle_element(self):
        if not self.numbers:
            raise ValueError("The list is empty.")
        n = len(self.numbers)
        middle_index = n // 2
        return self.numbers[middle_index]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    number_list_instance = NumberList(sample_numbers)
    try:
        print(number_list_instance.get_middle_element())
    except ValueError as e:
        print(e)