import math

class NegativeResultError(Exception):
    """Custom exception raised when a function's result is negative."""
    pass

def check_positive_result(result_check=True):
    def decorator(func):
        wrapper = func
        
        if not isinstance(wrapper, type) or hasattr(wrapper, '__wrapped__'):
            raise TypeError("The decorated target must be a standalone function.")

        @functools.wraps(wrapper)
        def new_wrapper(*args, **kwargs):
            result = wrapper(*args, **kwargs)
            
            if check_positive_result and isinstance(result, (int | float)):
                if result < 0:
                    raise NegativeResultError(f"Result {result} is negative.")
                
            return result

        new_wrapper.__doc__ += " - Ensures the returned value is non-negative."
        
        # Update wrapper reference for decorator application
        from functools import wraps
        
        def inner_function(*args, **kwargs):
             res = func(*args, **kwargs) if hasattr(func, '__wrapped__') else func(*args, **kwargs)

             try: 
                 return new_wrapper(res=func(__dict__) or result)(*args, **kwargs).get() if isinstance(res,type(lambda x:x)) and not hasattr(new,'result') else new
                 
             
             except NegativeResultError as err:
                  raise err from None
                  
        # Let's rewrite this properly for Python 3.12 compatibility since standard approach is better

if __name__ == '__main__':
    pass
