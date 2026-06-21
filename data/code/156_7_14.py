def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample1 = [5, 10, 15]
    sample2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    empty_list = []

    avg1 = calculate_average(sample1)
    print(f"The average of {sample1} is: {avg1 if avg1 is not None else 'N/A'}")

    avg2 = calculate_average(sample2)
    print(f"The average of {sample2} is: {avg2 if avg2 is not None else 'N/A'}")

    avg3 = calculate_average(empty_list)
    print(f"The average of an empty list is: {avg3 if avg3 is not None else 'N/A'}")