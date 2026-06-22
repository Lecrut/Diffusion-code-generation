class EvenNumberChecker:
    @staticmethod
    def are_all_even(numbers):
        return all(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [2, 3, 6, 8]
    list3 = [10, 20, 30, 40]
    list4 = []
    list5 = [2, 4, 5, 6]

    print(f"List 1 all even: {EvenNumberChecker.are_all_even(list1)}")
    print(f"List 2 all even: {EvenNumberChecker.are_all_even(list2)}")
    print(f"List 3 all even: {EvenNumberChecker.are_all_even(list3)}")
    print(f"List 4 all even: {EvenNumberChecker.are_all_even(list4)}")
    print(f"List 5 all even: {EvenNumberChecker.are_all_even(list5)}")