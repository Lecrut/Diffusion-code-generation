class LargestFinder:
    def find_largest(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        largest = numbers[0]
        for number in numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = LargestFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [7]
    list4 = []
    
    print(f"Largest in {list1}: {finder.find_largest(list1)}")
    print(f"Largest in {list2}: {finder.find_largest(list2)}")
    print(f"Largest in {list3}: {finder.find_largest(list3)}")
    try:
        print(f"Largest in {list4}: {finder.find_largest(list4)}")
    except ValueError as e:
        print(e)