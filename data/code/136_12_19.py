class NumberFilter:
    def filter_numbers(self, numbers):
        even_divisible_by_3 = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
        odd_not_divisible_by_5 = [num for num in numbers if num % 2 != 0 and num % 5 != 0]
        return even_divisible_by_3, odd_not_divisible_by_5

if __name__ == '__main__':
    nf = NumberFilter()
    sample_numbers = [12, 18, 21, 25, 30, 35, 42, 45]
    even_divisible_by_3, odd_not_divisible_by_5 = nf.filter_numbers(sample_numbers)
    print("Even numbers divisible by 3:", even_divisible_by_3)
    print("Odd numbers not divisible by 5:", odd_not_divisible_by_5)