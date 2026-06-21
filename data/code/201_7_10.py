def avg(lst):
    return sum(lst) / len(lst) if lst else 0

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    data3 = []
    print(f"Average of {data1}: {avg(data1)}")
    print(f"Average of {data2}: {avg(data2)}")
    print(f"Average of {data3}: {avg(data3)}")