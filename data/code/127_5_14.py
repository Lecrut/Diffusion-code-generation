def odd_filter(numbers):
    return (num for num in numbers if num % 2 != 0)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = odd_filter(sample_data)
    print(list(filtered_numbers))