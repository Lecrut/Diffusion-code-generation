def average_pairs(numbers):
    return sum(pair for pair in ((numbers[i], numbers[i+1]) for i in range(0, len(numbers) - 1))) / (len(numbers) // 2)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    print(average_pairs(sample_numbers))