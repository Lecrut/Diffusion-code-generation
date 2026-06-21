def mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    print(f"Mean of {list1}: {mean(list1)}")
    print(f"Mean of {list2}: {mean(list2)}")