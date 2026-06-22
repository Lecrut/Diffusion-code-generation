def sort_three_numbers(a, b, c):
    numbers = [a, b, c]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

if __name__ == '__main__':
    sorted_numbers = sort_three_numbers(3, 1, 2)
    print(*sorted_numbers)