def find_middle(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle_index_1 = n // 2 - 1
        middle_index_2 = n // 2
        return (numbers[middle_index_1] + numbers[middle_index_2]) / 2

if __name__ == '__main__':
    sequence = [10, 20, 30, 40, 50]
    if len(sequence) > 0:
        result = find_middle(sequence)
        print(result)