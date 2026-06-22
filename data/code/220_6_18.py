def calculate_average(numbers: list) -> float:
    if not numbers:
        raise ValueError("The set is empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_set1 = [1, 2, 3]
    sample_set2 = [4, 5]
    sample_set3 = [6, 7, 8, 9]

    print(f"Average of {sample_set1}: {calculate_average(sample_set1)}")
    print(f"Average of {sample_set2}: {calculate_average(sample_set2)}")
    print(f"Average of {sample_set3}: {calculate_average(sample_set3)}")