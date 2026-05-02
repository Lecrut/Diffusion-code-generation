def compare_and_report(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 >= sum2:
        return sum1, list1
    else:
        return sum2, list2
if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [2, 4, 1, 9]
    sum_a, winner = compare_and_report(list_a, list_b)
    print(f"Sum of List A: {sum_a}")
    print(f"Winning List: {winner}")
    list_c = [10, 20]
    list_d = [1, 1, 1]
    sum_c, winner = compare_and_report(list_c, list_d)
    print(f"Sum of List C: {sum_c}")
    print(f"Winning List: {winner}")