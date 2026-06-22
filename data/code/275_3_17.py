class EvenCounter:
    @staticmethod
    def count_evens(numbers):
        return sum(1 for num in numbers if num % 2 == 0)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    result = EvenCounter.count_evens(sample_numbers)
    print(result)