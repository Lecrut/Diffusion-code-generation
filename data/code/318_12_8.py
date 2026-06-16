def compare_adjacent_pairs(numbers):
    report = []
    for i in range(len(numbers) - 1):
        num1 = numbers[i]
        num2 = numbers[i+1]
        if num1 < num2:
            relationship = "strictly less than"
        elif num1 >= num2:
            relationship = "greater than or equal to"
        else:
            relationship = "equal to"
        report.append((num1, num2, relationship))
    return report
if __name__ == '__main__':
    sample_numbers = [1.5, 3.0, 2.5, 2.5, 8.1, 7.9]
    comparison_results = compare_adjacent_pairs(sample_numbers)
    for num1, num2, relation in comparison_results:
        print(f"Comparing {num1} and {num2}: {relation}")