import numpy as np

def calculate_average(data):
    return np.mean(data)

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [5, 15, 25]
    list3 = []
    list4 = [7.5, 8.5, 9.5]

    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {list3}: {calculate_average(list3)}")
    print(f"Average of {list4}: {calculate_average(list4)}")