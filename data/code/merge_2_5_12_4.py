import threading
from typing import Any
class ThreadSafeDeepComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, obj1: Any, obj2: Any) -> bool:
        with self._lock:
            if type(obj1) != type(obj2):
                return False
            attributes_1 = set(dir(obj1)) - {'__class__', '__dict__', '__module__', '__weakref__'}
            attributes_2 = set(dir(obj2)) - {'__class__', '__dict__', '__module__', '__weakref__'}
            if attributes_1 != attributes_2:
                return False
            for attr in attributes_1:
                val1 = getattr(obj1, attr)
                val2 = getattr(obj2, attr)
                is_nested = isinstance(val1, (dict, list)) and not isinstance(val1, str)
                is_nested_2 = isinstance(val2, (dict, list)) and not isinstance(val2, str)
                if is_nested or is_nested_2:
                    try:
                        result = self.compare(val1, val2)
                        if not result:
                            return False
                    except Exception:
                        return False
                else:
                    if val1 != val2:
                        return False
            return True
if __name__ == '__main__':
    comparator = ThreadSafeDeepComparator()
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
    person1 = Person("Alice", 30)
    person2 = Person("Alice", 30)
    class DataHolder:
        def __init__(self, value: int):
            self.value = [value]
    holder1 = DataHolder(42)
    holder2 = DataHolder([42])                                                                                    
    result_persons = comparator.compare(person1, person2)
    print(f"Person comparison (Alice/30 vs Alice/30): {result_persons}")
    class ComplexObj:
        def __init__(self):
            self.data = {'nested': [1, 2], 'flag': True}
    obj_a = ComplexObj()
    obj_b = ComplexObj()                            
    result_complex = comparator.compare(obj_a, obj_b)
    print(f"Complex Object comparison: {result_complex}")
    class DifferentType:
        pass
    diff_obj1 = DifferentType()
    diff_obj2 = Person("Bob", 25)
    result_diff_types = comparator.compare(diff_obj1, diff_obj2)
    print(f"Different Type comparison: {result_diff_types}")