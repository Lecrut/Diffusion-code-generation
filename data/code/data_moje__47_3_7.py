def average_of_integers(numbers):
    return sum(numbers) / len(numbers)

def average_using_generator(numbers):
    total = sum(x for x in numbers)
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = average_using_generator(sample_values)
    print(result)