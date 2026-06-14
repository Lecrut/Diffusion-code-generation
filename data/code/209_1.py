def calculate_average(data):
    if not data:
        return 0.0
    return sum(data) / len(data)
if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    list2 = []
    list3 = [10.5, 20.5, 30.5]
    average1 = calculate_average(list1)
    average2 = calculate_average(list2)
    average3 = calculate_average(list3)
    print(f"Average of {list1}: {average1}")
    print(f"Average of {list2}: {average2}")
    print(f"Average of {list3}: {average3}")