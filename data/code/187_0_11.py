class NumberFinder:
    def find_max_element(self, numbers):
        return max(numbers)

if __name__ == '__main__':
    finder = NumberFinder()
    sample_list1 = [10, 5, 20, 8, 15]
    print(f"The largest element in {sample_list1} is: {finder.find_max_element(sample_list1)}")
    
    sample_list2 = [-5, -1, -10, -3]
    print(f"The largest element in {sample_list2} is: {finder.find_max_element(sample_list2)}")