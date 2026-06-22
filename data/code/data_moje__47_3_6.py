def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def compute_average_generator(numbers):
    if not numbers:
        return 0
    return sum(x for x in numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_average_generator(sample_data)
    print(result)