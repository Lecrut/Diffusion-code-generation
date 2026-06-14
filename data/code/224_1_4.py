def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [10.5, 20.5, 30.5]
    list4 = [-1, 5, 10]
    mean1 = calculate_mean(list1)
    mean2 = calculate_mean(list2)
    mean3 = calculate_mean(list3)
    mean4 = calculate_mean(list4)
    print(f"Mean of {list1}: {mean1}")
    print(f"Mean of {list2}: {mean2}")
    print(f"Mean of {list3}: {mean3}")
    print(f"Mean of {list4}: {mean4}")