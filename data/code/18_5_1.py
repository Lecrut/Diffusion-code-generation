def greater_than_previous(sequence):
    if not sequence:
        return
    previous = sequence[0]
    for current in sequence[1:]:
        if current > previous:
            yield True
        previous = current
if __name__ == '__main__':
    data1 = [1, 3, 2, 5, 4]
    print("Data 1:")
    for result in greater_than_previous(data1):
        print(result)
    data2 = [1, 1, 2, 2, 3]
    print("\nData 2:")
    for result in greater_than_previous(data2):
        print(result)
    data3 = [5, 4, 3, 2, 1]
    print("\nData 3:")
    for result in greater_than_previous(data3):
        print(result)
    data4 = [1, 2, 3, 4]
    print("\nData 4:")
    for result in greater_than_previous(data4):
        print(result)