import sys
def check_non_decreasing(line):
    try:
        numbers = list(map(int, line.split()))
    except ValueError:
        return False
    if len(numbers) < 2:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    sample_input = "1 3 5 5 8"
    result = check_non_decreasing(sample_input)
    print(result)