import bisect

class ListCentralValue:
    def __init__(self, data):
        self.data = data
    
    def get_central_value(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("Cannot find the middle of an empty list")
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    central_value1 = ListCentralValue(sample_list1)
    print(f"Central value of {sample_list1}: {central_value1.get_central_value()}")
    
    sample_list2 = [10, 20, 30, 40, 50, 60]
    central_value2 = ListCentralValue(sample_list2)
    print(f"Central value of {sample_list2}: {central_value2.get_central_value()}")
    
    sample_list3 = [1, 2, 3, 4]
    try:
        central_value3 = ListCentralValue(sample_list3)
        print(f"Central value of {sample_list3}: {central_value3.get_central_value()}")
    except ValueError as e:
        print(e)