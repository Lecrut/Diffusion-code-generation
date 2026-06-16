import sys
def compare_adjacent_pairs(numbers):
    report = []
    for i in range(len(numbers) - 1):
        num1 = numbers[i]
        num2 = numbers[i+1]
        if num1 < num2:
            comparison = "strictly less than"
        elif num1 >= num2:
            comparison = "greater than or equal to"
        else:
            comparison = "error in comparison"
        report.append(f"Comparing {num1} and {num2}: {comparison}")
    return report
if __name__ == '__main__':
    sample_numbers = [1.5, 3.0, 2.5, 8.0, 8.0, 1.0, 0.5]
    report = compare_adjacent_pairs(sample_numbers)
    for line in report:
        print(line)