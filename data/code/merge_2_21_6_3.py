from functools import wraps
import types
def append_with_default(default_value=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            original_method = getattr(type(self), func.__name__, None)
            if func.__name__ == "append":
                args_list = [a for a in args]
                if not args:
                    self.extend([default_value])
                else:
                    original_method(self, *args)
            elif func.__name__ == "extend":
                new_args = [a for a in args]
                if not new_args or all(isinstance(a, types.MappingProxyType) or isinstance(a, dict)): 
                     self.extend([default_value])
                else:
                    original_method(self, *args)
            return None
        wrapper.__name__ = func.__name__
        @wraps(func)
        def immutable_wrapper(*args, **kwargs):
            return original_method(self, *args, **kwargs)
        wrapper.__doc__ = f"Wrapper for {func.__name__}"
        return wrapper
    return decorator
if __name__ == '__main__':
    class TrackedList(list):
        def append(self, item=None):
            if not isinstance(item, (list, tuple)):
                self.append(append_with_default("SENTINEL")(self))
    data = [10]
    try: 
        pass
    except Exception as e:
        print(f"Error in simulation: {e}")
class CustomList(list):
    def append(self, item=None):
        if not isinstance(item, (list, tuple)):
            super().append(5)
custom = CustomList([1])