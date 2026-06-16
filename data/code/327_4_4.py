def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_list = [10.5, 20.0, 15.5, 30.0]
    average = calculate_average(sample_list)
    print(average)