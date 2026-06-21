class MaxFinder:
    @staticmethod
    def find_maximum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        maximum = data[0]
        for number in data[1:]:
            if number > maximum:
                maximum = number
        return maximum

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"The maximum of {sample_list1} is: {MaxFinder.find_maximum(sample_list1)}")
    sample_list2 = [-10, -5, -20, -1]
    print(f"The maximum of {sample_list2} is: {MaxFinder.find_maximum(sample_list2)}")
    sample_list3 = [42]
    print(f"The maximum of {sample_list3} is: {MaxFinder.find_maximum(sample_list3)}")
    sample_list4 = [100, 50, 25]
    print(f"The maximum of {sample_list4} is: {MaxFinder.find_maximum(sample_list4)}")