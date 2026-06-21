def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    sample_lists = [[1, 2, 3, 4, 5], [10, 20, 30], [], [-1, 0, 1]]
    for lst in sample_lists:
        print(f"The average of {lst} is: {calculate_average(lst)}")