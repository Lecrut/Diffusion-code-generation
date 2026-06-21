import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    LIST_1 = [1, 2, 3, 4, 5]
    LIST_2 = [10.5, 20.5, 30.5]
    EMPTY_LIST = []
    LIST_3 = [-10, 20, 30]

    MEAN_1 = calculate_mean(LIST_1)
    MEAN_2 = calculate_mean(LIST_2)
    MEAN_EMPTY = calculate_mean(EMPTY_LIST)
    MEAN_3 = calculate_mean(LIST_3)

    print(f"Mean of {LIST_1}: {MEAN_1}")
    print(f"Mean of {LIST_2}: {MEAN_2}")
    print(f"Mean of {EMPTY_LIST}: {MEAN_EMPTY}")
    print(f"Mean of {LIST_3}: {MEAN_3}")