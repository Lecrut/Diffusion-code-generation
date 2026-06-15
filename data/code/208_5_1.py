def safe_mean(data):
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Data list contains non-numeric types.")
    return sum(data) / len(data)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    list3 = [1, 'a', 3]
    list4 = []
    print(f"Mean of {list1}: {safe_mean(list1)}")
    print(f"Mean of {list2}: {safe_mean(list2)}")
    try:
        safe_mean(list3)
    except TypeError as e:
        print(f"Error for {list3}: {e}")
    try:
        safe_mean(list4)
    except ZeroDivisionError as e:
        print(f"Error for {list4}: {e}")