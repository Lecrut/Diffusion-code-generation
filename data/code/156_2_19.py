AVERAGE_SAMPLE = [10, 20, 30, 40, 50]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    average = calculate_average(AVERAGE_SAMPLE)
    print(average)