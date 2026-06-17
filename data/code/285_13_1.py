def compare_adjacent(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i+1]:
            yield (numbers[i], numbers[i+1])
if __name__ == '__main__':
    data = [1.0, 2.5, 2.5, 3.0, 3.0, 1.1, 4.0]
    results = list(compare_adjacent(data))
    for pair in results:
        print(pair)