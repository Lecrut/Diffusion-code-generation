class EvenNumberFinder:
    START = 0
    END = 99

    @staticmethod
    def is_even(number):
        return number & 1 == 0

    @classmethod
    def find_evens(cls):
        evens = []
        for num in range(cls.START, cls.END + 1):
            if cls.is_even(num):
                evens.append(num)
        return sorted(evens)

if __name__ == '__main__':
    even_numbers = EvenNumberFinder.find_evens()
    print(even_numbers)