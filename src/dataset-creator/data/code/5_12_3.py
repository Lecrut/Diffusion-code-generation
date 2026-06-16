import threading
from typing import Any
class ThreadSafeDeepComparator:
    def __init__(self):
        self._lock = threading.Lock()
    @staticmethod
    def _deep_compare(obj1: Any, obj2: Any) -> bool:
        try:
            return isinstance(obj1, type) and isinstance(obj2, type)\
                and obj1.__name__ == obj2.__name__\
                and all(attr_name not in ('_lock', '__dict__', '_ThreadSafeDeepComparator') 
                       for attr_name in dir(obj1))\
                and getattr(obj1, 'value', None) is getattr(obj2, 'value', None)
        except Exception:
            return False
    def compare(self, obj1: Any, obj2: Any) -> bool:
        with self._lock:
            return ThreadSafeDeepComparator._deep_compare(obj1, obj2)
if __name__ == '__main__':
    comparator = ThreadSafeDeepComparator()
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
    person_a = Person("Alice", 30)
    person_b = Person("Bob", 25)
    class Container:
        def __init__(self, data):
            self.data = data
    container_x = Container([1, 2, 3])
    container_y = Container([4, 5, 6])
    result_1 = comparator.compare(person_a, person_b)
    result_2 = comparator.compare(container_x, container_y)
    print(f"Person comparison (Alice vs Bob): {result_1}")
    print(f"Container comparison ([1,2,3] vs [4,5,6]): {result_2}")