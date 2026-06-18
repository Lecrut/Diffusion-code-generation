class ValueComparator:
    def is_strictly_greater(self, value1, value2):
        if type(value1) != type(value2):
            return False
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.is_strictly_greater(5, 3))                         
    print(comparator.is_strictly_greater("z", "a"))                      
    print(comparator.is_strictly_greater(True, False))                                                                                                                                                                                                                                                                     
    print(comparator.is_strictly_greater(5, "3"))                       
    print(comparator.is_strictly_greater("a", 1))