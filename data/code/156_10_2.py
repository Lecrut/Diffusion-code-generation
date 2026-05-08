def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    mean1 = calculate_mean(sample_list)
    mean2 = calculate_mean(empty_list)
    print(f"The mean of {sample_list} is: {mean1}")
    print(f"The mean of {empty_list} is: {mean2}")