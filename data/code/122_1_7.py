def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    try:
        avg1 = calculate_average(list1)
        print(f"Average of {list1}: {avg1}")
        calculate_average(list2)
    except ZeroDivisionError as e:
        print(f"Error: {e}")