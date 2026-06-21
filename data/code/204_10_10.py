import statistics

def find_median(data):
    try:
        return statistics.median(data)
    except TypeError as e:
        raise ValueError("Input must be a list of numbers") from e

if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 5, 3, 4, 2]
    list3 = [10, 20, 30, 40]

    print(f"Median of {list1}: {find_median(list1)}")
    print(f"Median of {list2}: {find_median(list2)}")
    print(f"Median of {list3}: {find_median(list3)}")