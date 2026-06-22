def compute_average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_integers = [10, 20, 30, 40, 50]
    average = compute_average(sample_integers)
    print(average)