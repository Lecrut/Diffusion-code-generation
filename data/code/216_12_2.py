import sys
def find_middle(numbers):
    n = len(numbers)
    if n == 0:
        return None
    elif n % 2 == 1:
        return numbers[n // 2]
    else:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        return (middle1 + middle2) / 2
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    result = find_middle(sample_sequence)
    print(result)