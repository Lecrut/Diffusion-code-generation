from typing import Union

class Arithmetic:
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

if __name__ == '__main__':
    calc = Arithmetic()
    result_add = calc.add(5, 3)
    result_sub = calc.subtract(10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")