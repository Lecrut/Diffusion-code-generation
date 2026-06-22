class MiddleElementFinder:
    @staticmethod
    def find_middle_item(numbers):
        if not numbers:
            return None
        middle_index = len(numbers) // 2
        return numbers[middle_index]

if __name__ == '__main__':
    sample_odd_list = [1, 3, 5, 7, 9]
    sample_even_list = [2, 4, 6, 8, 10, 12]
    
    print("Middle element of the odd list:", MiddleElementFinder.find_middle_item(sample_odd_list))
    print("Middle element of the even list:", MiddleElementFinder.find_middle_item(sample_even_list))