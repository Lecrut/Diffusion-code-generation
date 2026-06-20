class ListAccess:
    @staticmethod
    def get_elements(lst):
        if not lst:
            return ()
        
        first = lst[0]
        last = lst[-1]
        
        if len(lst) % 2 == 0:
            middle_index = (len(lst) // 2) - 1
        else:
            middle_index = len(lst) // 2
        
        middle = lst[middle_index]
        
        return first, last, middle

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    result = ListAccess.get_elements(sample_list)
    print(result)