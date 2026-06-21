class OddNumberIdentifier:
    @staticmethod
    def is_odd(num):
        return num & 1

    @classmethod
    def find_odd_numbers(cls, numbers):
        return [num for num in numbers if cls.is_odd(num)]

if __name__ == '__main__':
    identifier = OddNumberIdentifier()
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = identifier.find_odd_numbers(sample_values)
    print(odd_numbers)