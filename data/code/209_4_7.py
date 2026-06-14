def calculate_average(data):
    try:
        if not data:
            return 0
        return sum(data) / len(data)
    except TypeError:
        raise TypeError("Input iterable contains non-numeric data.")
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = (10.5, 20.5, 30.5)
    sample3 = [1, 2, 'a', 4]
    sample4 = []
    print(f"Average of {sample1}: {calculate_average(sample1)}")
    print(f"Average of {sample2}: {calculate_average(sample2)}")
    try:
        calculate_average(sample3)
    except TypeError as e:
        print(f"Error for {sample3}: {e}")
    print(f"Average of {sample4}: {calculate_average(sample4)}")