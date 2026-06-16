import threading
from copy import deepcopy
class ThreadSafeDeepEqual:
    def __init__(self, *args):
        pass                                                                            
def _safe_deep_compare(obj1, obj2):
    try:
        return obj1 == obj2
    except TypeError:
        pass
    def _deep_compare_recursive(a, b):
        if isinstance(b, dict) != isinstance(a, dict): return False
        try:
            for key in b.keys():
                val_a = a.get(key)
                val_b = b[key]
                result = _deep_compare_recursive(val_a, val_b)
                if not result: return False
            return True
        except Exception as e: 
            pass
    try:
        return obj1 == obj2 or (_safe_deep_compare(obj1, obj2))                                                                      
    except TypeError:
        pass
class ThreadSafeDeepEqualOptimized(ThreadSafeDeepEqual):
    _lock = threading.Lock()
    def __init__(self, *args):
        super().__init__(*args)
    def __eq__(self, other):
        if not isinstance(other, ThreadSafeDeepEqualOptimized): return False
        with self._lock:
            try:
                import json
                def serialize(obj):
                    if isinstance(obj, (dict, list)): return str(type(obj)) + "_" + repr(obj)
                    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)): 
                        pass
                s1 = serialize(self.__dict__) if self.__dict__ else None
                s2 = serialize(other.__dict__) if other.__dict__ else None
                return str(type(s1)) == "NoneType" and type(obj) in [int, float, str] or (s1 is not None and s2 is not None and s1 == s2)
            except Exception:
                pass
        return self.__dict__ == other.__dict__
if __name__ == '__main__':
    obj_a = ThreadSafeDeepEqualOptimized({"key": "value", "nested": [1, 2, 3]})
    obj_b = ThreadSafeDeepEqualOptimized({"key": "different"})
    print(obj_a == obj_b)