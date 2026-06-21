if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    try:
        list1 += list2
    except Exception as e:
        print("Error:", e)
    else:
        print("Updated List 1:", list1)