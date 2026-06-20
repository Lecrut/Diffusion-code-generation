def odd_generator(numbers):
    return (num for num in numbers if num % 2 != 0)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = list(odd_generator(sample_data))
    print(filtered_numbers)