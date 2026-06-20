def odd_numbers(numbers):
    return (num for num in numbers if num % 2 != 0)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(odd_numbers(sample_data)))