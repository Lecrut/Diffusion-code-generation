def sum_list(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    list1 = [1.5, 2.7, 3.0, 4.2]
    list2 = [-10.5, 5.0, 0.1, 9.9]
    list3 = [3.14, 2.718, 1.618]
    sum1 = sum_list(list1)
    print(f"The sum of {list1} is: {sum1}")
    sum2 = sum_list(list2)
    print(f"The sum of {list2} is: {sum2}")
    sum3 = sum_list(list3)
    print(f"The sum of {list3} is: {sum3}")