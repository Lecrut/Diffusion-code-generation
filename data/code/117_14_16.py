from typing import Union

class NumberComparator:
    def __init__(self, value1: Union[int, float], value2: Union[int, float]):
        self.value1 = value1
        self.value2 = value2

    def signed_difference(self) -> Union[int, float]:
        return (self.value1 - self.value2)

if __name__ == '__main__':
    comparator1 = NumberComparator(10, 5)
    comparator2 = NumberComparator(-5, 100)
    
    print(f"Signed difference between {comparator1.value1} and {comparator1.value2}: {comparator1.signed_difference()}")
    print(f"Signed difference between {comparator2.value1} and {comparator2.value2}: {comparator2.signed_difference()}")