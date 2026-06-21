def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
    print(calculate_mean(sample_numbers))