def compare_adjacent(iterable):
    for i in range(len(iterable) - 1):
        a = iterable[i]
        b = iterable[i+1]
        yield b > a
if __name__ == '__main__':
    data1 = [1, 3, 2, 5, 4]
    print("Data 1 comparisons:")
    for result in compare_adjacent(data1):
        print(result)
    data2 = [10, 5, 8, 2, 9]
    print("\nData 2 comparisons:")
    for result in compare_adjacent(data2):
        print(result)
    data3 = [1, 1, 1, 1]
    print("\nData 3 comparisons:")
    for result in compare_adjacent(data3):
        print(result)