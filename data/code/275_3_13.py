class EvenCounter:
    @staticmethod
    def count_evens(numbers):
        even_count = 0
        for number in numbers:
            if number % 2 == 0:
                even_count += 1
        return even_count

if __name__ == '__main__':
    sample_data = [3, 4, 5, 6, 7, 8, 9]
    result = EvenCounter.count_evens(sample_data)
    print(result)